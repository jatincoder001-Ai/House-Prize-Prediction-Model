import pandas as pd
import sklearn.preprocessing as sp
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

def train_and_save():
    # 1. Load Data
    df = pd.read_csv('C:\\Users\\RUDRA\\OneDrive\\Apps\\Desktop\\Jatin 2.0\\pratice\\house_prediction\\Housing.csv')
    cleaned_df = df.copy()

    # 2. Encoding categorical variables
    encoder = sp.OneHotEncoder()
    cat_cols = cleaned_df.select_dtypes(include=['object']).columns
    encoded_cat = encoder.fit_transform(cleaned_df[cat_cols])
    encoded_cat_df = pd.DataFrame(encoded_cat.toarray(), columns=encoder.get_feature_names_out(cat_cols))
    final_df = pd.concat([cleaned_df.drop(cat_cols, axis=1), encoded_cat_df], axis=1)

    # 3. Scaling numerical features
    int_col = final_df.select_dtypes(include=['int64']).columns.drop('price')
    scaler = sp.MinMaxScaler()
    final_df[int_col] = scaler.fit_transform(final_df[int_col])

    # 4. Scaling the target (price)
    prize_scaler = sp.MinMaxScaler()
    final_df['price'] = prize_scaler.fit_transform(final_df[['price']])

    # 5. Splitting data
    X = final_df.drop('price', axis=1)
    y = final_df['price']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 6. Training the Linear Regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # 7. Print accuracy metric
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    print(f"Model trained. Train R^2: {train_score:.4f}, Test R^2: {test_score:.4f}")

    # 8. Save all assets to a pickle file
    assets = {
        'model': model,
        'encoder': encoder,
        'scaler': scaler,
        'prize_scaler': prize_scaler,
        'cat_cols': list(cat_cols),
        'int_col': list(int_col)
    }

    with open('C:\\Users\\RUDRA\\OneDrive\\Apps\\Desktop\\Jatin 2.0\\pratice\\house_prediction\\model_assets.pkl', 'wb') as f:
        pickle.dump(assets, f)
    print("Model assets saved successfully to model_assets.pkl")

if __name__ == "__main__":
    train_and_save()
