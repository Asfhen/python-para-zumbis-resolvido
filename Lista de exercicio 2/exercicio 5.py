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

def menor(a, b, c):
    min = a
    
    if b < min:
        min = b
    if c < min:
        min = c
        
    return min

print('O maior número é: ', maior(a, b, c))
print('O menor número é: ', menor(a, b, c))