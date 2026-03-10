# Task 2: Using the Math Module for Calculations

import math

# taking value by input module from the user
num = float(input("Enter a number: "))

# calculating values using from math module
square_root = math.sqrt(num)  #sqrt() module
natural_log = math.log(num)   #log() module
sine_value = math.sin(num)    #sin() module

# displaying results
print("Square root:", square_root)
print("Natural logarithm (log base e):", natural_log)
print("Sine (in radians):", sine_value)