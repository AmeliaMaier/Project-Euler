'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
'''
'''
# temp_list = [range(3, 1000000000000000, 2)]

not_primes = set([])
count = 1
for possible_prime in range(3,10000000000,2):
    if not(possible_prime in not_primes):
        #print(possible_prime)
        count +=1
        print(count)
        if (count == 10001): #get a memory error when I switch to 10001
            print (possible_prime)
            break
    else:
        not_primes.remove(possible_prime)
    for multiple in range(2,10000):
        #print(len(not_primes))
        not_primes.add(possible_prime*multiple)
'''

possible_primes = [True]*2369620
count = 0
for possible_prime, is_prime in enumerate(possible_primes):
    if possible_prime == 0 or possible_prime == 1:
        continue
    if is_prime:
        count += 1
        if(count == 1000):
            print(possible_prime)
            break
        for not_prime in range(possible_prime,len(possible_primes),possible_prime):
            possible_primes[not_prime] = False


'''
[1,2,3,4,...]
[3.5.7.9.11.13]
''
