# BMI Calculator 🔥

## 📌 About

This is a simple **BMI (Body Mass Index) Calculator** made using Python.

The program takes your **height in centimeters** and **weight in kilograms**, then calculates your BMI and displays your BMI category.

## 📐 BMI Formula
```text
BMI = Weight (kg) / Height² (m)
```

## 💻 Python Code

```python
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
```
## 📌 Example Output

```text
Enter your height in centimeters (cm): 170
Enter your weight in kilograms (kg): 67

Your Body Mass Index (BMI) is: 23.18
You are healthy
```

## ⚙️ How It Works

1. Enter your height in centimeters.
2. Enter your weight in kilograms.
3. The program converts height into meters.
4. BMI is calculated using the BMI formula.
5. The program displays your BMI.
6. It shows your BMI category.

## 🛠️ Requirements

- Python 3
- No external libraries required.
