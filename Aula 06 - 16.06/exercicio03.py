# #03 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
# maiores.
maior=0
menor=0
for c in range(0,7):
    idade = int(input('Qual o ano do seu nascimento?'))
    if (2021-idade) >= 18:
        maior += 1
    else:
        menor += 1
print(f'Existem {menor} menores de idade no grupo e {maior} maiores de idade no grupo')