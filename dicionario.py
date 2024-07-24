def criarUser():
    parar = 'parar'
    oi = ''
    while oi != parar:
        user = input('digite o usuario: ')
        cpf = input('digite o cpf: ')
        kk = {user:cpf}
        users = {user:cpf}
        users.update(kk)
        oi = input('se quiser continuar digite qualquer coisa, se quiser parar digite parar: ')
    print(users)

criarUser()








