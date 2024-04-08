#! python3
"""
Ask the user for their name and their email address.
(2 points)

Inputs:
 name
 email

Sample output:
 Your name is Joe Lunchbox, and your email is joe@koolsandwiches.org.

example:
What is your name:Dwayne Johnson
What ir your email:rock@aol.com

Your name is Dwayne Johnson, and your email is rock@aol.com
(aol? does dwayne johnson also use netscape navigator?)

What is your name:Jackie Chan
What ir your email:crazyAsian@qq.com

Your name is Jackie Chan, and your email is crazyAsian@qq.com

"""
N = input("Hello! What is your name? ")
EM = input("I will also need your email. ")
print(f"Your name is {N}, and your email is {EM}, did i get that correct?")