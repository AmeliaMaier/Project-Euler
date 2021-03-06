'''
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural
numbers and the square of the sum.
'''
sum_of_squares = 0
square_of_sums = 0

for num in range(1, 101, 1):
    sum_of_squares += num**2
    square_of_sums += num
square_of_sums = square_of_sums**2
print (square_of_sums-sum_of_squares)
