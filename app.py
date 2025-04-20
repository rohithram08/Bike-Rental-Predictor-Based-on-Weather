from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle

# Initialize Flask App
app = Flask(__name__)

# Load trained model
model = pickle.load(open('model/rental_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        temp = float(request.form['temp'])
        hum = float(request.form['hum'])
        wind = float(request.form['wind'])

        # Prediction
        features = np.array([[temp, hum, wind]])
        prediction = model.predict(features)
        result = int(prediction[0])

        return render_template('index.html', prediction_text=f'Estimated Daily Rentals: {result}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
