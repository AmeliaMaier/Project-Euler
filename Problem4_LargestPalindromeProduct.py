import math
possible_palindrome = 999*999
smallest_possible_factor = 100
answer_found = False
#continues until the correct palindrome is found
while(answer_found == False and possible_palindrome >= 100*100):
    #continues until a palindrome is found, starting from largest possible value of 2 3 digit numbers
    while (str(possible_palindrome)!= str(possible_palindrome)[::-1]):
        possible_palindrome = possible_palindrome - 1
    #check if it has 2 whole number multipiers with 3 digits
    x = 999
    while(x>=100):
        if(possible_palindrome%x == 0):
            print (possible_palindrome)
            answer_found = True
            break
        x = x - 1
    possible_palindrome = possible_palindrome - 1
