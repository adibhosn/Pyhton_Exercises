




matriz = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    for j in range(4):
        if i < j:
            matriz[i][j] = 2*i + 2*j
        elif i > j:
            matriz[i][j] = 3*i + 3*j
        else:
            matriz[i][j] = 4*i + 4*j
print(matriz)

