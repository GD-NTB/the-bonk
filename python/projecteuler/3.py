# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

answer = 0

from math import sqrt, trunc

num = 600851475143
multiple, prime = num, 1
primes = [ ]

while True:
    multiple = int(multiple / prime)
    primes.append(prime)

    for j in range(2, int(sqrt(multiple))):
        if multiple % j == 0:
            prime = j
            break
    
    if multiple/prime - trunc(multiple/prime) != 0: break

primes.append(multiple)
answer = max(primes)

print(answer)