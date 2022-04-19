from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("Sales_xg.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # User_ID
        #User_ID = request.form["User_ID"]

        # Product_ID
        #Product_ID = request.form["Product_ID"]

        #Gender
        Gender = request.form["Gender"]
        Gender_value=0
        if Gender == 'F':
            Gender_value = 0
        elif Gender == 'M':
            Gender_value = 1

        #Age
        age_value=0
        age = int(request.form["Age"])
        if age >= 0 and age <= 17:
            age_value = 1
        elif age >= 18 and age <= 25:
            age_value = 2
        elif age >= 26 and age <= 35:
            age_value = 3
        elif age >= 36 and age <= 45:
            age_value = 4
        elif age >= 46 and age <= 50:
            age_value = 5
        elif age >= 51 and age <= 55:
            age_value = 6
        elif age >= 56:
            age_value = 7

        #City_Category
        #City_Category_value=0
        #City_Category = request.form["City_Category"]
        #if(City_Category == 'A'):
        #   City_Category_value = 0
        #elif(City_Category == 'B'):
         #   City_Category_value = 1
        #elif(City_Category == 'C'):
         #   City_Category_value = 2


        #Marital_Status_value=0
        #Marital_Status = request.form["Marital_Status"]
        #if Marital_Status == "yes":
        #   Marital_Status_value =1
        #else:
         # Marital_Status_value =0

        # Stay_In_Current_City_Years
        Stay_In_Current_City_Years = int(request.form["Stay_In_Current_City_Years"])

        # Product_Category_1
        Product_Category_1 = int(request.form["Product_Category_1"])

        # Product_Category_2
        Product_Category_2 = int(request.form["Product_Category_2"])

        # Occupation
        Occupation = int(request.form["Occupation"])



       #['Gender', 'Age', 'Occupation', 'City_Category',
       #'Stay_In_Current_City_Years', 'Marital_Status', 'Product_Category_1',
       #'Product_Category_2']

        prediction = model.predict([[
            Gender_value,
            age_value,
            Occupation,
            Stay_In_Current_City_Years,
            Product_Category_1,
            Product_Category_2,
        ]])

        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text="Your Purchase is Rs. {}".format(output))

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
