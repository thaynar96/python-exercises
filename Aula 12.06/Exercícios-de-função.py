# Faça um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições:


def voto(ano):
    idade = 2021 - ano
    if idade < 16:
        return 'Voto negado'
    elif 16<=idade<18 or idade >= 70:
        return 'Voto opcional'
    else: 
        return 'Voto obrigatório'
ano = int(input('Ano de nascimento:'))
print(voto(ano))


# Faça um programa, com uma função que necessite de um parametro. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.

def vem(n):
    if n>0:
        return 'P'
    else:
        return 'N'

resultado = vem(int(input('Informe um número:')))
print(resultado)

# Faça um programa em Python com uma função que necessite de três parametros, e que forneça:
# A soma desses três parametros através de uma função.
# Seu script também deve fornecer a média dos três números,  através de uma segunda função que chama a primeira.

def numeros(n1,n2,n3):
        valor = n1 + n2 + n3
        return valor
        
def media_func():
    media = numeros(float(input('Nota 1: ')),int(input('Nota 2: ')),int(input('Nota 3: ')))/3
    return media

print(f'A média é {media_func():.2f}')


    