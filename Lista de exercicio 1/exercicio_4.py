salario = float(input(print('Digite o valor do salario: ')))
aumento = float(input(print('Digite o valor do aumento(em decimais): ')))
val_aum = salario * aumento
novo = salario + val_aum
print(f'O valor do aumento é de R${val_aum:.2f} e o salario é R${novo:.2f}')