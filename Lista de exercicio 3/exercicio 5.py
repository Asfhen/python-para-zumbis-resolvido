n = int(input("Digite n: "))
m = int(input("Digite m: "))

anterior  = n
atual     = m

r = atual % anterior
while r != 0:
    r = anterior % atual;
    anterior = atual;
    atual = r;

print(f'O menor divisor comum de ({n},{m}) é: {anterior}')