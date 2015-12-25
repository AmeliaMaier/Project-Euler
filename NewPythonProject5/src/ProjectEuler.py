# Work done based on Project Euler to practice recreational math & Python
# Open Source Project

import sys
import os

def main_menu():
    options_list = ('Problem 1: Find the sum of all multiples of x or y below z.', 'Problem 2: Find the sum of the even-valued terms in the Fibonacci sequesnce whose values do not exceed x.', 'Problem 3: Find the largest prime factor of x.')
    print ("Main Menu")
    for name in options_list: 
        print(name)
    main_menu_input = input("Which problem would you like solved? ")
    if main_menu_input == 1:
        problem_one()
    elif main_menu_input == 2:
        problem_two()
    elif main_menu_input == 3:
        problem_three()
    else:
        print("That is not a valid option.")

def problem_one():
    possible_multiple = 1 
    sum = 0
    x = input('Enter a value for X: ')
    y = input('Enter a value for Y: ')
    z = input('Enter a value for Z: ')
    while possible_multiple < z:
        if possible_multiple % x == 0:
            sum = sum + possible_multiple
        elif possible_multiple % y == 0:
            sum = sum + possible_multiple
        possible_multiple = possible_multiple + 1
    print 'The sum of all the mutlipes of ', x, ' or ', y, ' below ', z, ' is ', sum
    
def problem_two():
    final_sum = 0
    low = 1
    high = 1
    temp_sum = 0
    x = input('Enter a value for X: ')
    while high < x:
      temp_sum = high + low
      if temp_sum % 2 == 0:
        final_sum = final_sum + temp_sum
      low = high
      high = temp_sum
    print(final_sum)
      
def problem_three():
    list_of_factors = []
    current_possible_factor = 2
    x = input('Enter a value for X: ')
    current_total = x
    while current_total != 1:
        if current_total % current_possible_factor == 0:
            list_of_factors.append(current_possible_factor)
            current_total = current_total/current_possible_factor
            current_possible_factor = 2
        else:
            current_possible_factor = current_possible_factor + 1
    print'The largest prime factor of ', x, ' is ', max(list_of_factors), '.'     
main_menu()

