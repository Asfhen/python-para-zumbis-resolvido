y = int(input('Digite o ano: '))

if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print(f'{y} é um ano bissexto')
else:
    print(f'{y} não é um ano bissexto')