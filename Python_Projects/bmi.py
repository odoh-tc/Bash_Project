def bmi_calculator(x):
    if 18.5 <= x <= 24.9:
        print("Your BMI falls within the healthy weight range");
    elif x < 18.5:
        print("Your BMI falls within the underweight range");




height = float(input("Enter your height value in meter: "));
weight = float(input("Enter your weight value in kg: "));
value = weight / (height * height);
bmi_calculator(value);
