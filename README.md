# Heart Disease Prediction using Machine Learning

**Author:** D V Shriram

**Registration Number:** 23MIM10044

**Application Number:** IN26010538

**Batch Number:** 1A

**Email ID:** shriram.23mim10044@vitbhopal.ac.in

## Render Deployment-

https://heartdiseasedeployment-bqlu.onrender.com

## GitHub Repository-

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

This project successfully developed and deployed a machine learning model for heart disease prediction using the Random Forest algorithm. The model achieved good accuracy in predicting whether a patient is at risk of heart disease based on clinical parameters. A Flask REST API was created to serve predictions, and the application was successfully deployed on Render with the source code managed through GitHub. During deployment, challenges such as dependency management and Python version compatibility were encountered and resolved by configuring the required packages correctly. This project demonstrates the importance of MLOps practices, including version control, model serialization, API development, and cloud deployment. Overall, it provides practical experience in building and deploying an end-to-end machine learning application that can be accessed as a live web service.

