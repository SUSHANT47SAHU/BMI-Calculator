# Project Statement: BMI Calculator

---

## 1. Problem Statement

The Body Mass Index (BMI) is one of the common methods of screening where an individual's weight is measured relative to the height of the individual. The calculation of the body mass index manually requires unit conversion, squaring the height value, and performing divisions. This method is time-consuming and prone to errors, particularly for individuals who are unfamiliar with the formula.

This paper offers a simple command-line program that will calculate the BMI of an individual using the height and weight values of the individual and determine the category of weight.
---

## 2. Scope of the Project

**In scope**

- Input of Height in Centimeter and Weight in Kilogram from User
- Conversion of Height from Centimeter to Meter
- Calculation of BMI according to the formula `BMI = weight (kg)/height (m)2` 
- Display of BMI in 2 Decimal Places
- Categorization of the BMI (Severely Underweight, Underweight, Normal, Overweight, Severely Overweight)
- Display of Message when the calculated Value is not Valid
- Execution of the Code with only Python 3 without any Library

**Out of scope**

- Health diagnosis (BMI is just an indicative tool)
- Graphic/Website Interface
- User data storage or storing the history of BMI
- Adjustments based on age, gender, or muscle mass
- Imperial system (feet, inches, pounds)

---

## 3. Target Users

- Novices and students of Python who need to witness the application of input statements, mathematical operations, and conditional operators
- People seeking a fast method of calculating their BMI without performing manual calculations
- Teachers and reviewers searching for an easy-to-understand Python program example

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
