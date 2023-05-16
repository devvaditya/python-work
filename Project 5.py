# BMI2.0 Calculator
height = input("Enter Your Height in m: ")
weight = input("Enter your Weight in kgs: ")
bmi = int(float(weight)/(float(height) ** 2))
print(f"Your BMI(Body Mass Index) is : {bmi}")
if bmi < 18.5:
    print("You're Underweight.")
elif 18.5 <= bmi < 25:
    print("You have a normal weight.")
elif 25 <= bmi < 30:
    print("You are overweight.")
elif 30 <= bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")


