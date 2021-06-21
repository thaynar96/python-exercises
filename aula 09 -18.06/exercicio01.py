# Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if, verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade' e  também quantos são maiores e quantos são menores de idade.

lista = []
maior=menor=0
for c in range(5):
    nome = input('Escreva seu nome: ')
    idade = int(input('Escreva sua idade: '))
    if idade>18:
        maior+=1
    else:
        menor+=1
    lista.append([nome,idade])
        
print(lista, maior )

for i, c in enumerate(lista):
    if lista[i][1] > 18:
        print(f'{lista[i][0]} é maior de idade')
    else:
        print (f'{lista[i][0]} é menor de idade')
print (f'{maior} pessoas são maiores de idade e {menor} pessoas menores de idade.')
