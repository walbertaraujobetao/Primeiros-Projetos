usuario = input('Digite seu nome: ').strip().upper()
senha = int(input('Digite sua senha: '))

usuario_bd = 'BETO'
senha_bd = 123456

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado!')
else:
    print('Nome ou senha incorretos!')
        