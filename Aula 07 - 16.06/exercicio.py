# 01 - Crie um programa que vai gerar cinco números aleatórios de 1 a 50 e colocar em uma  tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla. Sem utilizar repetições.
# Dica: utilizar a biblioteca random do Python.

import random

n1 = random.randint(1,50)
n2 = random.randint(1,50)
n3 = random.randint(1,50)
n4 = random.randint(1,50)
n5 = random.randint(1,50)
tupla = (n1,n2,n3,n4,n5)
tupla_ordem = sorted((n1,n2,n3,n4,n5))

print(f'A listagem de numeros é {tupla}. O menor valor da tupla é {tupla_ordem[0]} e o maior {tupla_ordem[len(tupla_ordem)-1]} ')



# 02 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
tupla = ()
x = y =0
for c in range (1,5):
    valores = tuple(
    input('Escreva um número:'))
    tupla += valores
x = tupla.count('9')
y = tupla.index('3')
print(f'O número nove apareceu {x} vezes e o primeiro valor 3 apareceu na posição {y}')


# 03 - Dada a lista l = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# a) tamanho da lista.
# b) maior valor da lista.
# c) menor valor da lista.
# d) soma de todos os elementos da lista.
# e) lista em ordem crescente.
# f) lista em ordem decrescente.

lista = [5, 7, 2, 9, 4, 1, 3]

tamanho = len(lista)
maior = max(lista)
menor = min(lista)
soma = sum(lista)
crescente = sorted(lista)
decrescente = sorted(lista, reverse=True)

print(f'''

A lista tem {tamanho} itens.
O maior valor da lista é {maior}
O menor valor dda lista é {menor}
A soma de todos os itens da lista é {soma}
A lista em ordem crescente: {crescente}
A lista em ordem decrescente: {decrescente}
''')



# 04- Desafio da noite:
# Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
# "Telefonou para a vítima?"
# "Esteve no local do crime?"
# "Mora perto da vítima?"
# "Mora perto da vítima?"
# "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
# entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
# Caso contrário, ele será classificado como "Inocente".


lista = [
    "Telefonou para a vítima?\n[S/N]: ",
    "Esteve no local do crime?\n[S/N]: ",
    "Mora perto da vítima?\n[S/N]: ",
    "Devia para a vítima?\n[S/N]: ",
    "Já trabalhou com a vítima?\n[S/N]:   "
    ]
culpa = 0
for index, item in enumerate(lista):
    resposta = input(lista[index]).lower().split()[0]
    if resposta.startswith("s"):
        culpa += 1

while True:
    if culpa == 5:
        print('Você é o assassino')
        break
    elif 3<= culpa <=4:
        print('Você é cumplice')
        break
    elif culpa == 2:
        print('Você é um rapaz suspeito')
        break
    else: 
        print('Vá para casa pequeno gafanhoto')
        break
print('Interrogatório finalizado')


