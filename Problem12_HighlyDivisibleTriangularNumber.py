'''
The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

import math

divisors = []
triangle_num = 0
max_len = 0
for maximum in range(500,2000000):
    triangle_num = 0
    divisors = []
    for num in range(1,maximum):
        triangle_num += num
    for divisor in range (1,int(math.sqrt(triangle_num)+1)):
        if triangle_num%divisor == 0:
            divisors.append(divisor)
            divisors.append(triangle_num/divisor)
    if len(divisors) > max_len:
        max_len = len(divisors)
        print(max_len)
        print (triangle_num)
    if len(divisors) >500:
        print (triangle_num)
        break
