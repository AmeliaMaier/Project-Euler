import math

primeNumberList = []
current = 600851475143

#need to determine how to find prime factors
#print largets prime factor of max
while current%2 ==0:
    primeNumberList.append(2)
    current = current/2

for possible in range(3, int(math.sqrt(current))+1, 2):
    while current % possible == 0:
        primeNumberList.append(possible)
        current = current/possible
if current > 2:
    primeNumberList.append(current)

print (max(primeNumberList))
