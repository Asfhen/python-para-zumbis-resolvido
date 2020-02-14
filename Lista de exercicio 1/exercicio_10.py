cigarros = int(input(print('Digite a quantidade de cigarros fumados por dia: ')))
anos = int(input(print('Digite a quantos anos você fuma: ')))
dias = anos * 365
total = dias * cigarros
total_dias = 24 * 6
tmp_perdido = int(total / total_dias)
print('Você perdeu %d dias de vida' %tmp_perdido)