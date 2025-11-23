# -*- coding: utf-8 -*-

"""
5.	Design a module math_utils.py with functions:
factorial(n)
is_prime(n)
gcd(a,b)
Include exception handling for invalid or negative inputs. Import and test these functions from another script.
Concepts: Loops, recursion, functions, input validation.

"""

import math_utils
n = input("Please insert a number to calculate factorial and check if its prime ")
math_utils.factorial(n)
math_utils.is_prime(n)
x = input("Please input first number to check GCD ")
y = input("Please input second number to check GCD ")
math_utils.gcd(x,y)

