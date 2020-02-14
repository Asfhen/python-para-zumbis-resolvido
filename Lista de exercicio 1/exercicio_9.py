km = float(input(print('Digite a quantidade de kilometros percorridos: ')))
dia = int(input(print('Digite por quantos dias você pegou o carro: ')))
val_km = km * 0.15
val_dia = dia * 60
total = val_dia + val_km
print(f'O valor a se pagar e de: R${total:.2f}')