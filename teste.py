usuarios = []
qntd = input("Digite quantos usuarios deseja adicionar: ")


while int(len(usuarios)) < int(qntd):
    add = input('adicione elementos da lista')
    usuarios.append(add)

def pesquisar(usuario):
    usuario_encontrado = False
    for i in usuarios:
        if i == usuario:
            print('user encontrado')
            usuario_encontrado = True
            break
    if not usuario_encontrado:
        print('usuario não encontrado')



pesquisa = input('digite o nome que voce deseja encontrar')
pesquisar(pesquisa)