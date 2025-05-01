# 🚢 Titanic Survival Predictor

This is a machine learning web application that predicts whether a passenger would have survived the Titanic disaster based on their personal and travel details. It uses a trained classification model integrated into a responsive web interface.

---

## 📌 Features

- 🧠 Predicts survival using ML model (e.g., Logistic Regression / Random Forest)
- 📊 Inputs include class, sex, age, family size, fare, and embarkation port
- 🎨 Fully responsive UI with gradient background and animations
- ⚡ Built with **Flask** and served via a lightweight HTML/CSS frontend

---

---

## 🔍 Input Parameters

| Field       | Description                         | Example       |
|-------------|-------------------------------------|---------------|
| Pclass      | Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd) | 3           |
| Sex         | Gender                              | male / female |
| Age         | Age in years                        | 29            |
| SibSp       | # of siblings/spouses aboard        | 1             |
| Parch       | # of parents/children aboard        | 0             |
| Fare        | Ticket fare                         | 7.25          |
| Embarked    | Port of Embarkation (S, C, Q)       | S             |

---

## 🚀 Getting Started

### 1. Clone the repository

git clone https://github.com/Mazid2003/Titanic-survival-prediction-a-Data-Science-project.git

cd titanic-survival-predictor

2. Install requirements

pip install -r requirements.txt

3. Run the Flask app

python app.py

\Then open your browser at http://127.0.0.1:5000/

**🛠 Tech Stack**

Python

Flask

HTML5, CSS3

Machine Learning (scikit-learn / joblib)

Responsive Design

```
**📁 Project Structure**

├── app.py
├── model.pkl
├── templates/
│   └── index.html
├── static/
│   └── styles.css (if separated)
├── requirements.txt
└── README.md
```

✅ Example Prediction

Input:

Pclass: 3

Sex: male

Age: 35

SibSp: 0

Parch: 0

Fare: 7.25

Embarked: S

Prediction:

❌ Did Not Survive

**Screenshots**

![screenshot_2025-04-29_19-38-24](https://github.com/user-attachments/assets/f2eab517-1cb5-487a-9363-bd91bb659d37)
![screenshot_2025-04-29_19-39-37](https://github.com/user-attachments/assets/cad1d5b0-0e77-4221-a01d-d2d27ec8a9c9)
![screenshot_2025-04-29_19-39-09](https://github.com/user-attachments/assets/fbd980a0-71cd-4609-82c8-754b9c8bbf84)


**📄 License**

This project is licensed under the MIT License - feel free to use and modify!


