# #04 - Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
# Mostre também quantos valores pares foram digitados.

s = 0
pares =0
for c in range(0,6):
    n = int(input('Digite um número inteiro:'))
    if n % 2 ==0:
        s +=n
        pares += 1 
    else:
        s
print(f'A soma dos {pares} números pares digitados é {s}')