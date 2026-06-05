# MaternalCare AI

A smart health assistant for pregnant women, built as a Master's project in Software Engineering.

## Team

- Ramya Mercy Rajan
- Yada Thadathanacharoen
- Celestine Anyaegbunam Ugwu

**Department:** M.Sc. Software Engineering  
**University:** University of Europe for Applied Sciences

## Features

| Tab | What it does |
|-----|--------------|
| **BMI Calculator** | Calculates Body Mass Index from weight and height |
| **Delivery Date** | Estimates due date and weeks pregnant from last menstrual period (LMP) |
| **Risk Prediction** | Uses a Random Forest machine learning model to predict low, mid, or high maternal health risk |

## Tech stack

- **Python** — programming language
- **Streamlit** — web app interface
- **pandas** — load and work with the CSV dataset
- **scikit-learn** — train the Random Forest classifier

## How to run

1. **Clone this repository**

   ```bash
   git clone <your-repo-url>
   cd maternalcare-app
   ```

2. **Install libraries**

   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Download the dataset** from Kaggle:  
   [Maternal Health Risk Data](https://www.kaggle.com/datasets/csafrit2/maternal-health-risk-data)

4. **Rename the file** to `maternal_health_risk.csv` and place it in the project folder (same folder as `app.py`).

5. **Run the app**

   ```bash
   python -m streamlit run app.py
   ```

6. Open the URL shown in the terminal (usually http://localhost:8501).

## Project structure

```
maternalcare-app/
├── app.py                    # Main Streamlit app (all three tabs)
├── bmi_module.py             # BMI calculation and classification
├── edd_module.py             # Expected delivery date and weeks pregnant
├── risk_module.py            # Load CSV, train model, predict risk
├── maternal_health_risk.csv  # Dataset (download separately — not in repo)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Risk prediction module

The `risk_module.py` file:

1. Loads `maternal_health_risk.csv` with pandas
2. Uses features: Age, SystolicBP, DiastolicBP, BS, BodyTemp, HeartRate
3. Trains a Random Forest Classifier to predict `RiskLevel` (low / mid / high risk)
4. Exposes `predict_maternal_risk()` for the Streamlit app

## Disclaimer

This app is for **educational and research purposes only**. It is not a medical device and must not be used for clinical diagnosis or treatment decisions. Always consult a qualified healthcare professional.
