#01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.
# lista = []
# while True:
#     numeros = int(input('Escreva um valor numérico: '))
#     lista.append(numeros)
#     set(lista)
#     terminar = input('Você quer finalizar? [S/N]: ').strip().lower()[0]
#     if terminar =='s':
#         break
#     elif terminar=='n':
#         continue
#     else: 
#         print('Reinicie e escreva S ou N.')
#         break

# print(f'{sorted(set(lista))}')

lista = []
while True:
    numeros = int(input('Escreva um valor numérico: '))
    while numeros not in lista:
        lista.append(numeros)
    terminar = input('Você quer finalizar? [S/N]: ').strip().lower()[0]
    if terminar =='s':
        break
    elif terminar=='n':
        continue
    else: 
        print('Reinicie e escreva S ou N.')
        break
print(f'{sorted(lista)}')
