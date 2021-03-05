while True:
    n = int(input('digite a nota: '))
    if n >=0 and n <=10:
        print(f'{n} é uma nota valida')
        break
    else:
        print(f'{n} não é uma nota valida, por favor digite outra nota')