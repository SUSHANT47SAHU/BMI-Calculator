{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f1002f76-86f6-4527-8109-07b3ac908095",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your height in centimeters (cm):  180\n",
      "Enter your weight in kilograms (kg):  72\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Your Body Mass Index (BMI) is: 22.22\n",
      "You are healthy\n"
     ]
    }
   ],
   "source": [
    "# Take height in cm and weight in kg as input \n",
    "height_cm = float(input(\"Enter your height in centimeters (cm): \"))\n",
    "weight_kg = float(input(\"Enter your weight in kilograms (kg): \"))\n",
    "\n",
    "# Convert height from centimeters to meters\n",
    "height_m = height_cm / 100\n",
    "\n",
    "# Calculating BMI \n",
    "bmi = weight_kg / (height_m ** 2)\n",
    "\n",
    "# Displaying the calculated BMI\n",
    "print(\"Your Body Mass Index (BMI) is:\", round(bmi, 2))\n",
    "\n",
    "# Checking the BMI category\n",
    "if bmi > 0:\n",
    "    if bmi <= 16:\n",
    "        print(\"You are severely underweight\")\n",
    "    elif bmi <= 18:\n",
    "        print(\"You are underweight\")\n",
    "    elif bmi <= 25:\n",
    "        print(\"You are healthy\")\n",
    "    elif bmi <= 30:\n",
    "        print(\"You are overweight\")\n",
    "    else:\n",
    "        print(\"You are severely overweight\")\n",
    "else:\n",
    "    # Display this message if invalid values are entered\n",
    "    print(\"Please enter valid height and weight values.\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
