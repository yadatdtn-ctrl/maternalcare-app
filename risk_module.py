# Maternal Risk Prediction Module

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def load_data(filepath="maternal_health_risk.csv"):
    """
    Load the maternal health dataset from a CSV file.
    Returns a pandas DataFrame (think of it as a spreadsheet in Python).
    """
    data = pd.read_csv(filepath)
    return data


def prepare_features_and_target(data):
    """
    Split the dataset into:
    - features (X): the health measurements the model learns from
    - target (y): the risk level we want to predict
    """
    feature_columns = ["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"]
    X = data[feature_columns]
    y = data["RiskLevel"]
    return X, y


def train_model(X, y):
    """
    Train a Random Forest Classifier on the features and target.
    Returns the trained model, ready to make predictions.
    """
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    return model


def predict_risk(model, age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate):
    """
    Predict the risk level for one patient using their health measurements.
    Returns text: 'low risk', 'mid risk', or 'high risk'.
    """
    patient_data = pd.DataFrame(
        [[age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]],
        columns=["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"],
    )
    prediction = model.predict(patient_data)
    return prediction[0]


_trained_model = None
_model_accuracy = None


def _ensure_model_ready(filepath="maternal_health_risk.csv"):
    """
    Train once on 80% of the data and evaluate on the held-out 20%.
    The same model used for predictions is the one whose accuracy we report.
    """
    global _trained_model, _model_accuracy

    if _trained_model is None:
        data = load_data(filepath)
        X, y = prepare_features_and_target(data)
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        _trained_model = train_model(X_train, y_train)
        predictions = _trained_model.predict(X_test)
        _model_accuracy = round(accuracy_score(y_test, predictions) * 100, 1)

    return _trained_model, _model_accuracy


def predict_maternal_risk(age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate):
    """
    Main function for the app: load data, train the model (once), and predict risk.
    Returns text: 'low risk', 'mid risk', or 'high risk'.
    """
    model, _ = _ensure_model_ready()

    return predict_risk(
        model, age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate
    )


def get_model_accuracy(filepath="maternal_health_risk.csv"):
    """
    Return accuracy for the same model that makes live predictions.
    Measured on 20% of the dataset held out during training.
    """
    _, accuracy = _ensure_model_ready(filepath)
    return accuracy


if __name__ == "__main__":
    risk = predict_maternal_risk(
        age=25, systolic_bp=130, diastolic_bp=80, bs=15, body_temp=98, heart_rate=86
    )
    print(f"Predicted risk level: {risk}")
    print(f"Model accuracy: {get_model_accuracy()}%")