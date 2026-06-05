# Maternal Risk Prediction Module.
# Loads the CSV dataset, trains a Random Forest model, and predicts risk levels.

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# Load the maternal health dataset from a CSV file.
def load_data(filepath="maternal_health_risk.csv"):
    data = pd.read_csv(filepath)
    return data


# Split the dataset into feature columns (X) and the target label (y).
def prepare_features_and_target(data):
    feature_columns = ["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"]
    X = data[feature_columns]
    y = data["RiskLevel"]
    return X, y


# Train a Random Forest Classifier on the given features and target.
def train_model(X, y):
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    return model


# Predict the risk level for one patient using a trained model.
def predict_risk(model, age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate):
    patient_data = pd.DataFrame(
        [[age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]],
        columns=["Age", "SystolicBP", "DiastolicBP", "BS", "BodyTemp", "HeartRate"],
    )
    prediction = model.predict(patient_data)
    return prediction[0]


_trained_model = None
_model_accuracy = None


# Train the model once (80% of data) and cache it along with its test accuracy.
def _ensure_model_ready(filepath="maternal_health_risk.csv"):
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


# Main function for the app: train (if needed) and return a risk prediction.
def predict_maternal_risk(age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate):
    model, _ = _ensure_model_ready()
    return predict_risk(
        model, age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate
    )


# Return the accuracy of the same model used for live predictions.
def get_model_accuracy(filepath="maternal_health_risk.csv"):
    _, accuracy = _ensure_model_ready(filepath)
    return accuracy


if __name__ == "__main__":
    risk = predict_maternal_risk(
        age=25, systolic_bp=130, diastolic_bp=80, bs=15, body_temp=98, heart_rate=86
    )
    print(f"Predicted risk level: {risk}")
    print(f"Model accuracy: {get_model_accuracy()}%")
