# Work done based on Project Euler to practice recreational math & Python
# Open Source Project

import sys
import os

main_menu()

def main_menu():
    options_list = ('Problem 1: Find the sum of all multiples of x or y below z.', 'Problem 2: Find the sum of the even-valued terms in the Fibonacci sequesnce whose values do not exceed x.', 'Problem 3: Find the largest prime factor of x.')
    print ("Main Menu")
    for name in options_list: 
        print(name)
    main_menu_input = input("Which problem would you like solved? ")
    if main_menu_input == '1':
        problem_one()
    elif main_menu_input == '2':
        problem_two()
    elif main_menu_input == '3':
    else:
    print("That is not a valid option.")

def problem_one():
    multiple_x, multiple_y, count, sum = 0
    x = input('Enter a value for X: ')
    y = input('Enter a value for Y: ')
    z = input('Enter a value for Z: ')
    while multiple_x < z:
        count= count + 1
        multiple_x = count*x
        if multiple_x <= z:
            list_of_multiples.append(multiple_x)
            sum = sum + multiple_x
    count = 0
    while multiple_y < z:
        count= count + 1
        multiple_y = count*y
        if multiple_y <= z & multiple_y not in list_of_multiples:
            list_of_multiples.append(multiple_y)
            sum = sum + multiple_y
    print('The sum of all the mutlipes of ', x, ' or ', y, ' below ', z, ' is ', sum)
    