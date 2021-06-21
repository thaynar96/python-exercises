# #06 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:

# A) Quantas pessoas têm mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres têm menos de 20 anos.

maior_idade =0
homens = 0
mulheres =0
mulher_velha =0
while True:
    idade = int(input('Escreva a sua idade:'))
    sexo = input('Escreva "M" se você for mulher ou "H" se você for homem : ').upper().strip()[0]
    continua= input('Você quer continuar? [S/N] ').upper().strip()[0]

    if continua == 'S':
        if idade>=18:
            maior_idade+=1
        else:
            maior_idade

        if sexo == 'M':
            mulheres += 1
            if idade>20:
                mulher_velha += 1
        elif sexo == 'H':
            homens +=1
        else:
            print('O sexo precisa ser M ou H')
    elif continua == 'N':
        print('Você preferiu não continuar. Até mais!')
        break
print(f'''{maior_idade} são maiores de idade. 
{homens} homens se cadastraram e {mulher_velha} mulheres acima de 20 anos se cadastraram''')