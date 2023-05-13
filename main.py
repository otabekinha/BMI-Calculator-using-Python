print("Welcome to the BMI Calculator!")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = round(weight / height ** 2, 2)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, which means you are underweight.")
    suggestion = input("Do you need any suggestions regarding your BMI? (yes/no): ")
    if suggestion.lower() == "yes":
        print("You may want to consider increasing your calorie intake and incorporating strength training exercises to help build muscle mass.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, which means you are at a healthy weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, which means you are overweight.")
    suggestion = input("Do you need any suggestions regarding your BMI? (yes/no): ")
    if suggestion.lower() == "yes":
        print("You may want to consider reducing your calorie intake and increasing your physical activity to help lose weight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, which means you are obese.")
    suggestion = input("Do you need any suggestions regarding your BMI? (yes/no): ")
    if suggestion.lower() == "yes":
        print("You may want to consider consulting with a healthcare professional to create a personalized plan for weight loss and management.")
else:
    print(f"Your BMI is {bmi}, which means you are clinically obese.")
    suggestion = input("Do you need any suggestions regarding your BMI? (yes/no): ")
    if suggestion.lower() == "yes":
        print("You may want to consider seeking medical advice and support to manage your weight and reduce the risk of associated health conditions.")
