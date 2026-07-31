from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return "Heart Disease Prediction API"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    values = list(data.values())

    prediction = model.predict([values])[0]

    if prediction == 1:
        result = "Heart Disease Detected"
    else:
        result = "No Heart Disease"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)