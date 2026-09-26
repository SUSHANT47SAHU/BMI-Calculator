# BMI Calculator 🔥

A simple and beginner program **BMI (Body Mass Index) Calculator** made using Python.

This project takes the user's height and weight as input, calculates their BMI, and displays their BMI category.

---

## 📌 About BMI

**BMI (Body Mass Index)** is a value calculated using a person's weight and height.

It is calculated using the following formula:

```text
BMI = Weight (kg) / Height² (m)
```

The program uses the calculated BMI to display a basic weight category.

---

## ✨ Features

- Simple Python program
- Takes height in centimeters
- Takes weight in kilograms
- Converts height from centimeters to meters
- Calculates BMI automatically
- Displays BMI up to 2 decimal places
- Displays the BMI category
- Does not require external Python libraries

---

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

---

## 📌 Example Output

```text
Enter your height in centimeters (cm): 170
Enter your weight in kilograms (kg): 67

Your Body Mass Index (BMI) is: 23.18
You are healthy
```

---

## ⚙️ How It Works

The program works in a few simple steps:

1. The user enters their height in centimeters.
2. The user enters their weight in kilograms.
3. The program converts the height from centimeters to meters.
4. The BMI is calculated using the BMI formula.
5. The calculated BMI is displayed.
6. The program checks the BMI value.
7. The corresponding BMI category is displayed.

---

## 📊 BMI Categories

The program uses these ranges:

| BMI Range | Category |
|-----------|----------|
| 16 or below | Severely Underweight |
| 16.01 - 18 | Underweight |
| 18.01 - 25 | Healthy |
| 25.01 - 30 | Overweight |
| Above 30 | Severely Overweight |
---

## 🚀 Setup and Installation

Follow below to set up and run the project.

### Install Python

First, make sure that **Python 3** is installed on your computer.

You can download Python from the official Python website.

After installing Python, open a terminal and check the installed version:

```bash
python --version
```

You should see something similar to:

```text
Python 3
```
---

## ▶️ Running the Project

Make sure you are inside the project folder.

Run the program using:

```bash
python bmi_calculator.py
```

If your system uses `python3`, run:

```bash
python3 bmi_calculator.py
```

The program will ask you to enter your height and weight.

For example:

```text
Enter your height in centimeters (cm): 170
Enter your weight in kilograms (kg): 67
```

The program will then calculate and display your BMI.

---

## 📁 Project Structure

A simple project structure can look like this:

```text
BMI-Calculator/
│
├── bmi_calculator.py
├── README.md
```

## 🧮 BMI Calculation Example

Suppose:

```text
Height = 170 cm
Weight = 67 kg
```

First, the height is converted into meters:

```text
170 / 100 = 1.70 m
```

Then the BMI is calculated:

```text
BMI = 67 / (1.70 × 1.70)
BMI = 23.18
```

The program then displays:

```text
Your Body Mass Index (BMI) is: 23.18
You are healthy
```

---

## 🛠️ Requirements

- Python 3.x
- Basic command-line or terminal access
- No external Python libraries
---
