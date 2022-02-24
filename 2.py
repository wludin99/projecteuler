def fib(a,b):
    a,b = b, a+b
    yield a
    yield from fib(a,b)

f = fib(0,1)
for x in f:
    print(x)
    if x >= 20000000:
        break
