import math

def factor(n):
    prime = True
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            prime = False
            return [i] + factor(n/i)
    if prime:
        return [int(n)]

print(factor(100))

x = 1
for i in range(2,21):
    p = factor(i)
    for q in factor(x):
        if q in p:
            p.remove(q)
    x *= math.prod(p)
    print(x)
