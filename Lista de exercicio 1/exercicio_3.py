from datetime import datetime
dia_atual = datetime.today()
hora_atual = datetime.now()

dia = int(dia_atual.strftime('%d'))
dia_seg = dia * 86400
hora = int(hora_atual.strftime('%H'))
hora_seg = hora * 3600
minuto = int(hora_atual.strftime('%M'))
minuto_seg = minuto * 60
segundo = int(hora_atual.strftime('%S'))

data_seg = int(dia_seg + hora_seg + minuto_seg + segundo)
print('A data de hoje em segundos é: %d' %data_seg)