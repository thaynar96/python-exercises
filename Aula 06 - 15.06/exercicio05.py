# #05 - Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while
# sem break)
import random
n1 = int(input('Escreva o primeiro número:'))
n2 = int(input('Escreva o segundo número:'))
escolha = 0
while escolha < 5:
    print('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
    ''')
    escolha = int(input('Escreva o número da operação:'))
    if escolha == 1:
        print(n1 + n2)
    elif escolha == 2:
        print(n1 * n2)
    elif escolha == 3:
        if n1> n2:
            print('O primeiro número é maior que o segundo número')
        else:
            print('O  segundo número é maior que o primeiro')
    elif escolha == 4:
        n1 = random.randint(0,10)
        n2 = random.randint(0,10)
        print(f'O primeiro número agora é {n1} o segundo número agora é {n2}')

if escolha ==5:
    print('Você saiu do programa')