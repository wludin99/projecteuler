import math
n = 600851475143
prime_factors = []
def factor(n):
    prime = True
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            prime_factors.append(i)
            prime = False
            return factor(n/i)
    if prime:
        prime_factors.append(int(n))

factor(n)
print(prime_factors)
