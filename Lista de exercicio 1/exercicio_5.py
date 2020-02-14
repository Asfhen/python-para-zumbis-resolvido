preco = float(input(print('Digite o valor do produto: ')))
desco = float(input(print('Digite o percentual do disconto(em numeros decimais): ')))
valor_desco = preco * desco
total = preco - valor_desco
print(f'O valor do desconto é de {valor_desco:.2f} e o preço total é de {total:.2f}')