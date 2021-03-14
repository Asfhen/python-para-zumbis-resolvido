a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))

def maior(a, b, c):
    max = a
    
    if b > max:
        max = b
    if c > max:
        max = c
    
    return max

print('O maior número é: ', maior(a, b, c))