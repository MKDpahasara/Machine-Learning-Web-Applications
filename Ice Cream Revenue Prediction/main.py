from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the machine learning model (change 'model.pkl' to your model's file name)
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temperature = float(request.form['temperature'])
    prediction = model.predict([[temperature]])
    predicted_price = round(prediction[0], 2)
    return render_template('result.html', temperature=temperature, predicted_price=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)