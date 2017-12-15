'''
possible_palindrome = 999*999
answer_found = False
#continues until the correct palindrome is found
while(answer_found == False and possible_palindrome >= 100*100):
    #continues until a palindrome is found, starting from largest possible value of 2 3 digit numbers
    while (str(possible_palindrome)!= str(possible_palindrome)[::-1]):
        possible_palindrome = possible_palindrome - 1
    #check if it has 2 whole number multipiers with 3 digits
    x = 999
    while(x>=100):
        if(possible_palindrome%x == 0 and possible_palindrome/x >=100):
            print (possible_palindrome)
            answer_found = True
            break
        x = x - 1
    possible_palindrome = possible_palindrome - 1
'''

min=100
max=999
max_palindrome = 0
for x in range(min,max + 1):
    for y in range(x + 1, max + 1): # avoid duplicates
        prod = x*y
        if prod > max_palindrome and str(prod)==(str(prod)[::-1]):
            max_palindrome = prod
print (max_palindrome)
