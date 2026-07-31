# Heart Disease Prediction using Machine Learning

**Author:** D V Shriram

**Registration Number:** 23MIM10044

**Application Number:** IN26010538

**Batch Number:** 1A

**Email ID:** shriram.23mim10044@vitbhopal.ac.in

## Render Deployment

Render URL:

https://heartdiseasedeployment-bqlu.onrender.com

## GitHub Repository

https://github.com/dvshriram-dvs/HeartDiseaseDeployment.git

## Project Description

This project predicts whether a patient is likely to have heart disease using a Machine Learning model. A Random Forest Classifier is trained on the Heart Disease dataset and deployed as a Flask web application.

## Technologies Used

- Python
- Pandas
- Scikit-learn
- Flask
- Joblib
- Render
- GitHub

## Dataset

[Heart Disease Dataset from Kaggle](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)

## Algorithm

Random Forest Classifier

## Model Accuracy

Accuracy: 98.5%

## Project Structure

```
HeartDiseaseDeployment/
│
├── app.py
├── train_model.py
├── model.pkl
├── heart.csv
├── requirements.txt
├── README.md
```

## How to Run

1. Install dependencies

```
pip install -r requirements.txt
```

2. Run the Flask app

```
python app.py
```

3. Open

```
http://127.0.0.1:5000/
```
## Conclusion

The Random Forest model achieved good accuracy for predicting heart disease. The Flask API successfully accepts patient information and returns predictions in JSON format. The project demonstrates the complete machine learning deployment process using GitHub and Render, highlighting the importance of MLOps for version control, deployment, and serving machine learning models.