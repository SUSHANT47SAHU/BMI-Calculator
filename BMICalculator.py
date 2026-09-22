# Take height in cm and weight in kg as input 
height_cm = float(input("Enter your height in centimeters (cm): "))
weight_kg = float(input("Enter your weight in kilograms (kg): "))

# Convert height from centimeters to meters
height_m = height_cm / 100

# Calculating BMI 
bmi = weight_kg / (height_m ** 2)

# Displaying the calculated BMI
print("Your Body Mass Index (BMI) is:", round(bmi, 2))

# Checking the BMI category
if bmi > 0:
    if bmi <= 16:
        print("You are severely underweight")
    elif bmi <= 18:
        print("You are underweight")
    elif bmi <= 25:
        print("You are healthy")
    elif bmi <= 30:
        print("You are overweight")
    else:
        print("You are severely overweight")
else:
    # Display this message if invalid values are entered
    print("Please enter valid height and weight values.")
