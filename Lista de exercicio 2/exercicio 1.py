a = int(input('Digite o lado a: '))
b = int(input('Digite o lado b: '))
c = int(input('Digite o lado c: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Esses valores não podem formar um triangulo!')
elif (a==b) and (a==c):
    print('Esses valores formam um triangulo equilatero')
elif (a==b) or (a==c) or (b==c):
    print('Esses valores formam um triangulo isóceles')
else:
    print('Esses valores formam um triangulo escaleno')