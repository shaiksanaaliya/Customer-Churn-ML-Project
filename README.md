# Customer Churn Prediction ML Project

## Project Overview

This project predicts whether a customer is likely to churn using Machine Learning.

The trained machine learning model is deployed as a REST API using FastAPI and can be containerized using Docker.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Pydantic
- Uvicorn
- Joblib
- Docker

## Project Files

- `churn_model.pkl` — Trained machine learning model
- `app.py` — FastAPI REST API
- `requirements.txt` — Required Python packages
- `Dockerfile` — Docker configuration
- `test_api.py` — API unit tests
- `README.md` — Project documentation

## API Endpoint

### POST `/predict`

The API accepts customer information and returns a churn prediction and prediction probabilities.

Example response:

```json
{
  "prediction": 1,
  "churn_probability": 0.80,
  "no_churn_probability": 0.20
}tuning, evaluation, model selection, and model serialization.
