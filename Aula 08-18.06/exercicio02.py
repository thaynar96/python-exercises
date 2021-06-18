#02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.
lista = []
listaextra1= list()
listaextra2= list()
numeros =0
while True:
    numeros = int(input('Escreva seu número: '))
    lista.append(numeros)
    if numeros % 2 == 0:
        listaextra1.append(numeros)
    else:
        listaextra2.append(numeros)
    finalizar = input('Você quer finalizar? [S/N] :').upper().strip()[0]
    if finalizar == 'S':
        break
        

print(f'''
Lista completa: {lista}
Lista pares:{listaextra1}
Lista impares{listaextra2}''')