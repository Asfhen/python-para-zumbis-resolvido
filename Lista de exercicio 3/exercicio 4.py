n = int(input('n: '))
a, b = 1, 1
cont = 1
while cont <= n-2:
    print(a, b)
    a, b = b, a + b
    cont = cont + 1
print(f'fib({n}) = {b}')