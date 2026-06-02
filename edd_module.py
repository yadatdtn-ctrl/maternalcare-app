# Expected Delivery Date Module
from datetime import date, timedelta

def calculate_edd(Imp):
    edd = Imp + timedelta(days=280)
    return edd

def calculate_weeks(Imp):
    edd = Imp + timedelta(days=280)
    return edd

def calculate_weeks(Imp):
    today = date.today()
    days_passed = (today - Imp).days
    weeks = days_passed // 7
    return weeks

# Testing the functions
Imp = date(2025, 9, 1)
print(calculate_edd(Imp))
print(calculate_weeks(Imp))

