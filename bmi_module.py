# BMI Calculator Module
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal weight"
    else:
        return "Overweight"


#Testing the functions
bmi = calculate_bmi(70, 1.70)
print(bmi)

category = classify_bmi(bmi)
print(category)