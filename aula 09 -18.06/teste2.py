matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range (3):
    for c in range(3):
        matriz[l][c]= int(input('Digite um valor'))

for i,c in enumerate(matriz):
    print()
    print (matriz[i][c],end='')
    