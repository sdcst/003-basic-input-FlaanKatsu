#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

input("This program finds X in which A*X+B=C(Press enter)")
input("You will input values for A, B and C(Press enter)")
A = int(input("Please input A"))
B = int(input("Now please input B."))
C = int(input("Lastly, input C")) 

X = ( C - B  ) / A
print(f"The anwer is {X}")