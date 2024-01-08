from flask import Flask, render_template, request
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input from form
        year = int(request.form['Year'])
        present_price = float(request.form['Present_Price'])
        kms_driven = int(request.form['Kms_Driven'])
        fuel_type = int(request.form['Fuel_Type'])
        seller_type = int(request.form['Seller_Type'])
        transmission = int(request.form['Transmission'])
        owner = int(request.form['Owner'])

        # Make prediction using the loaded model
        prediction = model.predict([[year, present_price, kms_driven, fuel_type, seller_type, transmission, owner]])
        predicted_price = round(prediction[0], 2)

        return render_template('index.html', prediction_text=f'Predicted Selling Price: {predicted_price*400000} LKR')

if __name__ == '__main__':
    app.run(debug=True)
