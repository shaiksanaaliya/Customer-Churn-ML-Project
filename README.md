# Customer Churn ML

## Project Overview

This project develops a machine learning system to predict customer churn. Multiple classification algorithms are trained, tuned, compared, and evaluated to identify the best-performing model.

## Objectives

- Predict whether a customer is likely to churn.
- Compare multiple machine learning classification models.
- Perform hyperparameter tuning using GridSearchCV.
- Use Stratified K-Fold Cross-Validation.
- Evaluate models using Precision, Recall, F1-Score, and ROC-AUC.
- Select and save the best-performing model.

## Features Used

The model uses the following customer-related features:

- Tenure
- Support Tickets
- Monthly Spend
- Last Login Days
- Plan Type

## Machine Learning Models

Four classification models were trained and compared:

1. Logistic Regression
2. Random Forest
3. XGBoost
4. LightGBM

## Hyperparameter Tuning

GridSearchCV with Stratified K-Fold Cross-Validation was used to optimize model parameters.

## Model Evaluation

The models were evaluated using:

- Precision
- Recall
- F1-Score
- ROC-AUC
- Confusion Matrix
- Classification Report
- ROC-AUC Curves

## Champion Model

Based on the available test split, **Random Forest** was selected as the champion model.

| Model | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|
| Random Forest | 1.00 | 1.00 | 1.00 | 1.00 |

> Note: The dataset used for this project is very small, so the reported test metrics should not be interpreted as evidence of real-world 100% accuracy.

## Project Files

- `Customer_Churn_ML.ipynb` — Complete Jupyter Notebook
- `champion_model.joblib` — Saved Random Forest model
- `feature_names.joblib` — Saved feature information

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- Matplotlib
- Jupyter Notebook
- GitHub

## Conclusion

The project demonstrates a complete supervised machine learning workflow for customer churn prediction, including preprocessing, model training, hyperparameter tuning, evaluation, model selection, and model serialization.
