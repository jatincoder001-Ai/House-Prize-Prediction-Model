# 🏠 Estimo — Premium House Price Predictor

<div align="center">

### Predict House Prices Using Machine Learning 🤖

A modern web application that predicts the estimated market value of a house based on its features and specifications.

</div>

---

## 📸 Project Preview

### 🏠 Main Interface

<img width="1915" height="967" alt="Screenshot 2026-09-05 080910" src="https://github.com/user-attachments/assets/6a407f26-5808-46a0-ba9f-00765b1c48ae" />


### ⚙️ Property Features & Location

<img width="1905" height="911" alt="Screenshot 2026-09-05 080925" src="https://github.com/user-attachments/assets/17b4831c-a11f-4103-a247-08b1fe14ce81" />


### 💰 Prediction Result

<img width="1906" height="915" alt="Screenshot 2026-09-05 080939" src="https://github.com/user-attachments/assets/99ff6523-cea3-4da3-b6d7-a892573b954a" />


---

# ✨ Features

- 🏠 Predict house prices using Machine Learning
- 📐 Enter property area
- 🛏️ Select the number of bedrooms
- 🚿 Select the number of bathrooms
- 🏢 Select the number of floors
- 🚗 Add parking spaces
- 🛣️ Main road access option
- 🛋️ Select furnishing status
- ❄️ Air conditioning option
- 🔥 Water heater option
- ⭐ Preferred location option
- 🏡 Basement option
- 🛏️ Guestroom option
- 💰 Get an estimated market value

---

# 🤖 Machine Learning

This project uses a Machine Learning model to predict house prices based on different property features.

The model is trained using historical housing data and then used by the Flask application to generate predictions.

### 📊 Dataset

The dataset used for training:

```text
Housing.csv
```

### 💾 Trained Model

The trained Machine Learning model is saved as:

```text
model_assets.pkl
```

The Flask application loads this trained model and uses it to predict house prices based on the property details entered by the user.

---

# 🛠️ Technologies Used

### Backend

- 🐍 Python
- 🌶️ Flask

### Machine Learning & Data Science

- 🤖 Scikit-learn
- 🐼 Pandas
- 🔢 NumPy
- 💾 Joblib

### Frontend

- HTML
- CSS

---

# 📁 Project Structure

```text
House-Prediction-Model/
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   └── index.html
│
├── .gitignore
├── .gitattributes
├── app.py
├── Housing.csv
├── model_assets.pkl
├── requirements.txt
└── train_and_save.py
```

---

# 📌 Important Files

| File | Description |
|---|---|
| `app.py` | Main Flask backend application |
| `train_and_save.py` | Used to train and save the Machine Learning model |
| `Housing.csv` | Dataset used for training |
| `model_assets.pkl` | Saved trained Machine Learning model |
| `templates/index.html` | Main frontend page |
| `static/css/style.css` | Styling for the application |
| `requirements.txt` | Required Python libraries |

---

# 🚀 Getting Started

Follow these steps to run this project on your computer.

## 1️⃣ Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
```

---

## 2️⃣ Go Inside the Project Folder

```bash
cd YOUR-REPOSITORY-NAME
```

---

## 3️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

---

## 4️⃣ Activate the Virtual Environment

### 🪟 Windows

```bash
.venv\Scripts\activate
```

### 🐧 Linux / 🍎 Mac

```bash
source .venv/bin/activate
```

---

## 5️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Run the Application

```bash
python app.py
```

After running the application, open your browser and visit:

```text
http://127.0.0.1:5000
```

🎉 Your House Price Predictor should now be running!

---

# 🧠 How It Works

```text
Housing Dataset
       ↓
Data Preprocessing
       ↓
Machine Learning Model Training
       ↓
Save Trained Model
       ↓
Flask Backend
       ↓
User Enters House Details
       ↓
Model Makes Prediction
       ↓
Estimated House Price 💰
```

---

# 👨‍💻 About This Project

Hi! 👋

I'm a **14-year-old student and aspiring AI/ML Engineer** who is currently learning Python, Machine Learning, and software development.

This project is part of my learning journey. 🚀

The **UI/UX design was created with the help of AI**, while the **backend logic and Machine Learning implementation were written and implemented by me**.

I'm still learning, and I know there are many things that can be improved in this project.

I believe the best way to learn programming is by building real projects, making mistakes, fixing them, and continuously improving. 💪

Feedback, suggestions, and improvements are always welcome! ❤️

---

# 🔮 Future Improvements

Things I want to improve in the future:

- [ ] Improve the Machine Learning model
- [ ] Compare multiple ML algorithms
- [ ] Add better input validation
- [ ] Improve error handling
- [ ] Add proper model evaluation metrics
- [ ] Add prediction history
- [ ] Add charts and data visualization
- [ ] Improve mobile responsiveness
- [ ] Deploy the project online
- [ ] Add Docker support
- [ ] Add automated testing

---

# 🤝 Contributions

Contributions, ideas, and suggestions are welcome!

1. Fork the repository
2. Create a new branch
3. Make your improvements
4. Submit a Pull Request

---

# ⭐ Support

If you like this project, consider giving the repository a ⭐!

It motivates me to keep learning, building, and improving. 🚀

---

<div align="center">

### Built with ❤️ using Python, Flask & Machine Learning

**Learning • Building • Improving 🚀**

</div>
