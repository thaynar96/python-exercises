# #01 - Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com essa formatação:

# [  1  ][  2  ][  3  ]
# [  4  ][  5  ][  6  ]
# [  7  ][  8  ][  9  ] 

# linha_1 = input("Linha 1: Escreva 3 números separados por espaço").split()
# linha_2 = input("Linha 2: Escreva 3 números separados por espaço").split()
# linha_3= input("Linha 3: Escreva 3 números separados por espaço").split()

# matriz = [list(map(int, linha_1)),list(map(int, linha_2)),list(map(int, linha_3))]

# # matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for j in matriz:

#     print(f'''
#             [  {matriz[0][0]}  ][  {matriz[0][1]}  ][  {matriz[0][2]}  ]
#             [  {matriz[1][0]}  ][  {matriz[1][1]}  ][  {matriz[1][2]}  ]
#             [  {matriz[2][0]}  ][  {matriz[2][1]}  ][  {matriz[2][2]}  ]
#     ''')

matriz = []
somaPares= 0
terceira = 0
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Escreva um número da linha {i+1} e coluna {j+1}:'))
        linha.append(valor)
    matriz.append(linha)
for i in matriz:
    print()
    for j in i:
        print(f'[ {j} ]',end=' ')
        if j % 2 == 0:
            somaPares += j
    

print(f'A soma dos n pares {somaPares}')

# #02 - Aprimore o desafio anterior, mostrando no final:
#    A) A soma de todos os valores pares digitados.
#    B) A soma dos valores da terceira coluna. 
#    C) O maior valor da segunda linha.



#03 - Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista, depois do dado inserido, pergunte ao usuário se ele quer continuar, se ele não quiser pare o programa. No final mostre:
# Quantas pessoas foram cadastradas
# Mostre o maior peso
# Mostre o menor peso

# lista = []
# while True:
#     nome = input('Escreva seu nome: ')
#     peso = int(input('Escreva seu peso: '))
#     lista.append([nome,peso])
#     finalizar = input('Você quer finalizar? [S/N] ').strip().upper()[0]
#     if finalizar == 'S':
#         break
#     else:
#         continue
# print(lista)
# for i, c in enumerate(lista):
#     if lista[i][1] > 18:
#         print(f'{lista[i][0]} é maior de idade')
#     else:
#         print (f'{lista[i][0]} é menor de idade')
#         print (f'{maior} pessoas são maiores de idade e {menor} pessoas menores de idade.')
