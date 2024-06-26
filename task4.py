#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math
input("This program takes the hight and radius of a cone, and calculates the surface area.(press enter)")
R = int(input("please input the radius and press enter."))
H = int(input("please input the hight and press enter."))
SHX = R ** 2 + H ** 2
SH = SHX ** 0.5
SA = math.pi * R * SH + math.pi * R ** 2
print(f"the answer for surface area is {SA}.")