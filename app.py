from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)
model = pickle.load(open('titanic_model.pkl', 'rb'))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        try:
            Pclass = int(request.form['Pclass'])
            Sex = 1 if request.form['Sex'] == 'male' else 0
            Age = float(request.form['Age'])
            SibSp = int(request.form['SibSp'])
            Parch = int(request.form['Parch'])
            Fare = float(request.form['Fare'])
            Embarked = {'S': 0, 'C': 1, 'Q': 2}[request.form['Embarked']]
            FamilySize = SibSp + Parch + 1

            input_df = pd.DataFrame([{
                'Pclass': Pclass,
                'Sex': Sex,
                'Age': Age,
                'SibSp': SibSp,
                'Parch': Parch,
                'Fare': Fare,
                'Embarked': Embarked,
                'FamilySize': FamilySize
            }])

            result = model.predict(input_df)[0]
            prediction = "Survived ✅" if result == 1 else "Did Not Survive ❌"

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
