'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

largest_chain = 0
answer = 0
collatz_chain = [1]
current_step = 0
for num in range(999999, 1, -2):
    current_step = num
    collatz_chain = [1]
    while current_step != 1:
        collatz_chain.append(current_step)
        if current_step%2==0:
            current_step /= 2
        else:
            current_step = 3*current_step + 1
    if len(collatz_chain) > largest_chain:
        largest_chain = len(collatz_chain)
        answer = num
        print (num)
