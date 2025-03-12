# Exercises

# Reinforcement

# R-1.1

# Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.

# Solution
# def is_multiple(n, m):
#
#     return n % m == 0

# R-1.2
# Write a short Python function, is_even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

# solution
# Method 1: check if last digit is either 0, 2, 4, 6 or 8
# def is_even(k):
#     last_digit = str(k)[-1]
#     return last_digit in ['0', '2', '4', '6', '8']

# Method 2: using a bitwise AND operator between number and 1


# def is_even(k):
#     return k & 1 == 0
#
#
# print(is_even(127))

# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
#  one or more numbers, and returns the smallest and largest numbers, in the
#  form of a tuple of length two. Do not use the built-in functions min or
#  max in implementing your solution.

# solution

# def minmax(data):
#     minim = data[0]
#     maxim = data[0]
#     for num in data:
#         if num <= minim:
#             minim = num
#         elif num >= maxim:
#             maxim = num
#
#     return minim, maxim
#
#
# my_list = [5, 3, 23, 1, 94, -9]
# print(minmax(my_list))

# R-1.4 Write a short Python function that takes a positive integer n and returns
#  the sum of the squares of all the positive integers smaller than n.

# Solution

# def sumsquares(n):
#     squares = []
#     for num in range(n):
#         squares.append(num**2)
#     return sum(squares)
#
#
# print(sumsquares(7))

#  R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely
# ing on Python’s comprehension syntax and the built-in sum function.

# def sumsquares(n):
#     return sum(k**2 for k in range(n))
#
#
# print(sumsquares(7))

# R - 1.6 Write a short Python function that takes a positive integer n and
# returns the sum of the squares of all the odd positive integers smaller than n.

# def sum_odd_squares(n):
#     squares = []
#     for num in range(1, n, 2):
#         squares.append(num**2)
#
#     return sum(squares)
#
#
# print(sum_odd_squares(9))

# R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely
# ing on Python’s comprehension syntax and the built-in sum function.

# def sum_odd_squares(n):
#     return sum(k*k for k in range(1, n, 2))
#
#
# print(sum_odd_squares(10))

# R-1.8 Python allows negative integers to be used as indices into a sequence,
#  such as a string. If string s has length n, and expression s[k] is used for in
# dex −n≤k<0, what is the equivalent index j≥0such that s[j] references
#  the same element?

# R-1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

# Solution
# print(list(x for x in range(50, 81, 10)))

# R - 1.10 What parameters should be sent to the range constructor,
# to produce a range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

# Solution

# print(list(x for x in range(8, -9, -2)))

# R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

# Solution
# print(list(2**x for x in range(9)))


