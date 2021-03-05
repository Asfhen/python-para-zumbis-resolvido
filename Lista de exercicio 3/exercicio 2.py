user = input('Digite seu nome de usuario: ')
while True:
    psw = input('Digite sua senha: ')
    if psw == user:
        print('Sua senha não pode ser igual seu nome de usuario')
    else:
        print('Usuario e senha cadastrados!')
        break