# Project Statement: BMI Calculator

**Author:** Sushant Sahu
**Language:** Python 3

---

## 1. Problem Statement

Body Mass Index (BMI) is a widely used screening measure that relates a person's weight to their height. Calculating it by hand means converting units, squaring the height and dividing, and then comparing the result against category ranges. This is slow and easy to get wrong, especially for people who are not comfortable with the formula.

This project provides a simple command-line program that takes a person's height and weight, calculates their BMI automatically, and tells them which weight category the value falls into.

---

## 2. Scope of the Project

**In scope**

- Accepting height in centimeters and weight in kilograms from the user
- Converting height from centimeters to meters
- Calculating BMI using the formula `BMI = weight (kg) / height (m)²`
- Displaying the BMI rounded to 2 decimal places
- Classifying the BMI into a category (severely underweight, underweight, healthy, overweight, severely overweight)
- Showing a message when the calculated value is not valid
- Running with Python 3 alone, with no external libraries

**Out of scope**

- Medical diagnosis or health advice (BMI is only a general screening indicator)
- Graphical or web interface
- Storing user data or tracking BMI history
- Age-, gender-, or muscle-mass-specific adjustments
- Support for imperial units (feet, inches, pounds)

---

## 3. Target Users

- Beginners and students learning Python who want to see input, arithmetic, and conditional logic in a practical program
- Anyone who wants a quick way to check their BMI without doing the calculation manually
- Instructors and reviewers looking for a small, readable example of a Python program

---

## 4. High-Level Features

| Feature | Description |
|---|---|
| User input | Prompts for height (cm) and weight (kg) |
| Unit conversion | Converts height from centimeters to meters automatically |
| BMI calculation | Applies the standard BMI formula |
| Formatted output | Shows the BMI rounded to 2 decimal places |
| Category classification | Uses `if-elif-else` logic to report the weight category |
| Invalid value message | Prompts the user to enter valid values when the result is not positive |
| No dependencies | Uses only built-in Python, so it runs anywhere Python 3 is installed |

---

## 5. Disclaimer

This program is for learning and general information only. BMI does not account for body composition, age, or other factors, and the result should not replace advice from a qualified healthcare professional.
