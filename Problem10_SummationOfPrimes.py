'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million. (2000000)
'''
sum = 0
possible_primes = [True]*2000000
for possible_prime, is_prime in enumerate(possible_primes):
    if possible_prime == 0 or possible_prime == 1:
        continue
    if is_prime:
        sum += possible_prime
        for not_prime in range(possible_prime,len(possible_primes),possible_prime):
            possible_primes[not_prime] = False
print (sum)
