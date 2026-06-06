
def get_height():
    return float(input("Enter Your Height in meter (example 1.83): "))

def get_weight():
    return float(input("Enter Your Weight in kilogram (example 75): "))

def get_bmi():
    h = get_height()
    w = get_weight()
    bmi = w//h**2
    print(bmi)

    if bmi < 18.5:
        return f'Your BMI is {bmi} and your Underweight'
    elif 18.5 <= bmi < 25:
        return f'Your BMI is {bmi} and your Normal weight'
    elif 25 <= bmi < 30:
        return f'Your BMI is {bmi} and your 1st class of obesity'
    elif 30 <= bmi < 40:
        return f'Your BMI is {bmi} and your 2nd class of obesity'
    elif bmi > 40:
        return f'Your BMI is {bmi} and your 3th class of obesity'


if __name__ == '__main__':
    print(get_bmi())

