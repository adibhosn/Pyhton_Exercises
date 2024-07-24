matriz=[[7,4,9,2],[1,3,5,7],[2,1,8,9],[7,8,3,4]]
def trocar_por_zero(matriz):
    for linha in matriz:
        for posicao in linha:
            if posicao == matriz[0][0]:
                matriz[0][0] = 0
            elif posicao == matriz[1][1]:
                matriz[1][1] = 0
            elif posicao == matriz[2][2]:
                matriz[2][2] = 0
            elif posicao == matriz[3][3]:
                matriz[3][3] = 0
    print(matriz)
trocar_por_zero(matriz)