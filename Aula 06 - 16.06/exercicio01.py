# #01 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi
# o maior e o menor peso lidos.

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input(f'Informe o peso {c}: '))

    if c == 1:
        maior = peso
        menor = peso
            
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

        
print(f'O maior peso foi {maior}Kg e o menor peso foi {menor}Kg')