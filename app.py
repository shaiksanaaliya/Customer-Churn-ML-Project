from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI(
    title="Customer Churn Prediction API",
    description="REST API for predicting customer churn",
    version="1.0.0"
)

# Load trained model
model = joblib.load("churn_model.pkl")


class CustomerData(BaseModel):
    data: dict


@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running"
    }


@app.post("/predict")
def predict(customer: CustomerData):

    try:
        input_data = pd.DataFrame([customer.data])

        prediction = int(model.predict(input_data)[0])

        probability = model.predict_proba(input_data)[0]

        return {
            "prediction": prediction,
            "churn_probability": float(probability[1]),
            "no_churn_probability": float(probability[0])
        }

    except Exception as e:
        return {
            "error": str(e)
        }
