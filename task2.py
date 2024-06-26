#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

import math
input("I will help your calculate the volume of a sphere.(Press Enter to Continue)")
R = float(input("Please input the radius and press enter (Please only input numbers)"))
U = input("what unit are you using? (cm, ft, inch, etc)")
V = 4/3 * math.pi * ( R ** 3 )
print (f"If the radius of a sphere is {R} {U}, then its volume is {V} {U}.")