# 🚦 Road Accident Severity Prediction (RASP)

An end-to-end Machine Learning project with a Flask web application that predicts the **severity of road accidents** based on real-world traffic and environmental factors. This project aims to help authorities, transport departments, and drivers understand potential accident severity and take **proactive safety measures**.

---

## 🧠 Overview

The **Road Accident Severity Prediction System** analyzes multiple parameters like **day of the week, lighting conditions, vehicle type, speed limit, and road conditions** to classify the severity of an accident into one of three categories: _Slight_, _Serious_, or _Fatal_.

The model is built using a supervised learning approach, incorporating data preprocessing, feature engineering, and classification techniques. A clean and responsive **Flask-based web interface** allows users to input real-time or simulated data and instantly receive a prediction.

---

## 🎯 Objectives

- Predict the **severity of road accidents** using a machine learning model trained on historical data.
- Develop an **interactive web interface** using Flask for real-time predictions.
- Provide a tool that can help authorities make **data-driven safety decisions**.
- Demonstrate a **complete ML pipeline**, from data preprocessing and model training to deployment.

---

## ✨ Features

- ✅ **End-to-End ML Workflow:** Data cleaning → Model training → Web deployment
- ✅ **Data Preprocessing:** Handles missing values and encodes categorical variables using `LabelEncoder`
- ✅ **Robust Model:** Trained with a `RandomForestClassifier` for high accuracy and robustness
- ✅ **Dynamic Web App:** A user-friendly web form for real-time input and instant predictions
- ✅ **Responsive UI:** Modern and clean interface built with HTML, CSS, and Bootstrap
- ✅ **Persistent Model:** The trained model and encoders are saved using `joblib` for efficient reuse
- ✅ **Modular Codebase:** Well-structured and easy-to-maintain project layout

---

## ⚙️ Tech Stack

- **Languages:** Python, HTML5, CSS3
- **Libraries & Frameworks:** Flask, Scikit-learn, Pandas, NumPy
- **Tools:** Joblib, Git & GitHub, VS Code

---

## 📂 Project Structure

```plaintext
Road-Accident-Severity-Prediction/
├── app.py                      # Flask web application
├── train_model.py              # Script for training and saving the model
├── model.pkl                   # Trained RandomForestClassifier model
├── le_day.pkl                  # LabelEncoder for 'Day_of_Week'
├── le_light.pkl                # LabelEncoder for 'Light_Conditions'
├── le_severity.pkl             # LabelEncoder for 'Accident_Severity'
├── dataset.csv                 # Dataset for model training
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
│
├── templates/
│   └── index.html              # Frontend HTML template
│
└── static/
    └── style.css               # Custom CSS for styling
```

---

# 🚀 Getting Started

Follow these steps to set up and run the project on your local machine.

---

## 🧩 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Road-Accident-Severity-Prediction.git
cd Road-Accident-Severity-Prediction
```

---

## 🧠 2. Create and Activate a Virtual Environment

**On Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**

```bash
python -m venv venv
source venv/bin/activate
```

---

## 📦 3. Install Dependencies

Install all required libraries from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

If a `requirements.txt` file is not available, install packages manually:

```bash
pip install flask scikit-learn pandas numpy joblib
```

---

## 🧮 4. Train the Model

Run the training script to process the data and generate the model and encoder files:

```bash
python train_model.py
```

You should see a confirmation message upon successful completion:

```
Model and encoders saved successfully ✅
```

---

## 🌐 5. Run the Flask Web Application

Launch the Flask app to start the web server:

```bash
python app.py
```

Then open your web browser and navigate to:

👉 http://127.0.0.1:5000/

You can now input various parameters into the web form to get real-time accident severity predictions.

---

## 📈 Example Prediction

| Input                | Example Value          |
| -------------------- | ---------------------- |
| Day                  | Monday                 |
| Light Conditions     | Darkness - lights lit  |
| Sex of Driver        | Male (1)               |
| Vehicle Type         | Car (2)                |
| Speed Limit          | 60                     |
| Pedestrian Crossing  | No (0)                 |
| Road Type            | Single carriageway (1) |
| Special Conditions   | None (0)               |
| Number of Passengers | 2                      |

**Predicted Severity:** ✅ Serious

---

## 💡 Learnings & Conclusion

### Learnings

- **End-to-End Project Execution:** Gained hands-on experience in managing a full ML lifecycle — from data acquisition and cleaning to model deployment as a web service.
- **Feature Engineering:** Understood the importance of preprocessing categorical features using `LabelEncoder`.
- **Model Selection:** Used `RandomForestClassifier`, which performed well for classification tasks.
- **Web Development with Flask:** Learned to integrate trained ML models into a Flask web app for dynamic predictions.
- **Model Persistence:** Implemented `joblib` for saving/loading models efficiently.

### Conclusion

This project demonstrates that machine learning can effectively predict road accident severity. The model classifies potential accidents and provides insights for preventive actions. The Flask app serves as a simple, user-friendly interface, bridging ML and usability.

---

## 🔮 Future Enhancements

- 🌤️ **API Integration:** Use live weather and traffic data APIs for dynamic predictions.
- 🗺️ **Data Visualization:** Add interactive maps to visualize accident-prone zones.
- ☁️ **Cloud Deployment:** Deploy using Docker on AWS, Heroku, or Render.
- 🤖 **Advanced Models:** Experiment with XGBoost or Neural Networks for improved accuracy.
- 🌐 **Multi-language Support:** Add localization options to the web interface.

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. **Fork** the repository.
2. **Create a new branch:**
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Commit your changes:**
   ```bash
   git commit -m 'Add some feature'
   ```
4. **Push to the branch:**
   ```bash
   git push origin feature/YourFeature
   ```
5. **Open a Pull Request.**

⭐ If you found this project helpful, don’t forget to give it a star!

---
