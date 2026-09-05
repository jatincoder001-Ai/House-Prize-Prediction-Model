import os
import pickle
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load model and preprocessors at startup
assets_path = os.path.join(os.path.dirname(__file__), 'model_assets.pkl')
if not os.path.exists(assets_path):
    raise FileNotFoundError("model_assets.pkl not found! Please run train_and_save.py first.")

with open(assets_path, 'rb') as f:
    assets = pickle.load(f)

model = assets['model']
encoder = assets['encoder']
scaler = assets['scaler']
prize_scaler = assets['prize_scaler']
cat_cols = assets['cat_cols']
int_col = assets['int_col']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No input data provided'}), 400

        # Extract features and format/validate
        try:
            area = float(data.get('area', 0))
            bedrooms = int(data.get('bedrooms', 0))
            bathrooms = int(data.get('bathrooms', 0))
            stories = int(data.get('stories', 1))
            parking = int(data.get('parking', 0))
            
            mainroad = str(data.get('mainroad', 'no')).lower()
            guestroom = str(data.get('guestroom', 'no')).lower()
            basement = str(data.get('basement', 'no')).lower()
            hotwaterheating = str(data.get('hotwaterheating', 'no')).lower()
            airconditioning = str(data.get('airconditioning', 'no')).lower()
            prefarea = str(data.get('prefarea', 'no')).lower()
            furnishingstatus = str(data.get('furnishingstatus', 'semi-furnished')).lower()
        except (ValueError, TypeError) as e:
            return jsonify({'error': f'Invalid input format: {str(e)}'}), 400

        # Construct single-row DataFrame matching training layout
        input_data = {
            'area': [area],
            'bedrooms': [bedrooms],
            'bathrooms': [bathrooms],
            'stories': [stories],
            'mainroad': [mainroad],
            'guestroom': [guestroom],
            'basement': [basement],
            'hotwaterheating': [hotwaterheating],
            'airconditioning': [airconditioning],
            'parking': [parking],
            'prefarea': [prefarea],
            'furnishingstatus': [furnishingstatus]
        }
        
        feature_cols = [
            'area', 'bedrooms', 'bathrooms', 'stories', 'mainroad', 'guestroom', 
            'basement', 'hotwaterheating', 'airconditioning', 'parking', 'prefarea', 
            'furnishingstatus'
        ]
        
        input_df = pd.DataFrame(input_data)[feature_cols]

        # Apply One-Hot Encoding to categorical variables using the fitted encoder
        encoded_cat = encoder.transform(input_df[cat_cols])
        encoded_cat_df = pd.DataFrame(encoded_cat.toarray(), columns=encoder.get_feature_names_out(cat_cols))
        
        # Merge numerical columns and encoded categorical columns
        final_input_df = pd.concat([input_df.drop(cat_cols, axis=1), encoded_cat_df], axis=1)

        # Apply MinMaxScaler to the numerical features
        final_input_df[int_col] = scaler.transform(final_input_df[int_col])

        # Execute prediction
        scaled_prediction = model.predict(final_input_df)

        # Inverse transform the prediction target to get original price
        prediction_original = prize_scaler.inverse_transform(scaled_prediction.reshape(-1, 1))
        predicted_price = float(prediction_original[0][0])

        # Return formatted prediction result
        return jsonify({
            'success': True,
            'prediction': predicted_price,
            'formatted_prediction': f"₹{predicted_price:,.2f}"  # Assuming INR based on typical dataset price range, but styled nicely
        })

    except Exception as e:
        return jsonify({'error': f'Server prediction error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
