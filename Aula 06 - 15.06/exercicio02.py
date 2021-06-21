# #02 - Crie um programa que pergunte ao usuário um número inteiro e faça a
# tabuada desse número.
n = int(input("Escreva um número inteiro:"))
for count in range (1,11):
    print(f'{n} X {count} = {n*count}')