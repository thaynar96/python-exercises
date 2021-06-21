# #07 - Crie um programa que leia o nome e o preço de vários produtos. O programa
# deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000.
# (C) Qual é o nome do produto mais barato.

preco = 0
total = 0
mais_mil= 0
barato = 0
primeira_vez = True
while True:
    produto= input('Produto: ')
    preco = int(input('Preço R$: '))
    if primeira_vez == True:
        barato = preco
        produto_barato = produto
    if preco < barato :
        barato = preco
        produto_barato = produto
    primeira_vez = False
    total +=preco
    if preco>1000:
        mais_mil +=1    
    
    continuar = input('Deseja continuar? [S/N]: ')
    if continuar == 's':
        continue
    else:
        break

print(f'''
O valor total gasto: {total}
O número de itens acima de mil:{mais_mil}
O produto mais barato foi: {produto_barato.title()} pelo valor de R$ {barato}''')