# 1.Faça um programa, com uma função que necessite de três argumentos, e que forneça a
# soma desses três argumentos.

def func(a,b,c):
    soma = a + b + c
    print(soma)

func(4,5,3)

# 2. Faça um programa, com uma função que necessite de um argumento. A função retorna
# o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for
# negativo e ‘0’ se for 0.


def func(a):
    if a > 0:
        print('P')
    elif a < 0:
        print('N')
    else:
        print('0')

func(10)



# 3. Faça um programa com uma função chamada somaImposto. A função possui dois
# parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
# porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o
# valor de custo para incluir o imposto sobre vendas.


def somaImposto(taxaImposto,custo):
    custo = custo * (1 + taxaImposto/100)
    print(f'O valor total com a taxa de imposto é R${custo:.2f}')

taxa = float(input('Digite a taxa %:'))
custo = float(input('Custo do produto em R$:'))
somaImposto(taxa,custo)

# 4. Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário
# é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha
# mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def calculadora(salario,n):
    if n - 40>0: # o n representa as horas. 
        horas= n - 40 #Se as horas forem maior que 40 a subtração vai me dar as horas extras.
        total = horas * ( 20 * 1.5 )#as horas extras multiplicadas pelo valor de cada hora multiplicado pelo acrescimo.
        print(f'O salário desse més com ajuste é {salario + total}') #valor do salário + acrescimo de acordo com as horas 
    else:
        print(f'O seu salário não teve reajuste pois você não possui horas extras')

salario = float(input('Salário:'))
extra = float(input('Horas trabalhadas:'))

calculadora(salario,extra)

# 5. Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha
# 1,68 e pese 75kg.

def imc(altura,peso):
    f = peso/altura**2
    return f

altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

print(f'Seu IMC é {imc(altura,peso):.2f}')

# 6. Escreva uma função que, dado um número nota representando a nota de um estudante,
# converte o valor de nota para um conceito (A, B, C, D, E e F).
# Nota Conceito
# >=9.0 A
# >=8.0 B
# >=7.0 C
# >=6.0 D
# >=5.0 E
# <=4.0 F


def nota(n):
    if n>=9:
        n = 'A'
    elif n>=8:
        n = 'B'
    elif n>=7:
        n= 'C'
    elif n>=6:
        n= 'D'
    elif n>=5:
        n= 'E'
    elif n<=4:
        n= 'F'
    print(f'O seu conceito é {n}')
n = float(input('Escreva a nota que será transformada em conceito:'))

nota(n)

# 7. Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles
# forem iguais, imprima que eles são iguais.

def para(a,b):
    if a == b:
        print('Os parametros são iguais')
    elif a>b:
        print(f'O menor parametro é o {b:.2f}')
    elif a<b:
        print(f'O menor parametro é o {a:.2f}')

a = float(input('Paramentro 1:'))
b= float(input('Paramentro 2:'))

para(a,b)

# DESAFIO - Data com mês por extenso. Construa uma função que receba uma data no
# formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA.

# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que
# Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro
# terá 29 dias.
from datetime import date
def data(d):
    meses = ['','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    lista = d.split('/')
    lista = list(map(int, lista))
    
    if (lista[2] % 4 == 0 and lista[2] % 100 !=0) or lista[2] % 400 == 0:
        bissexto = True
    else:
        bissexto = False

    listaCondicoes = [
        lista[0] not in range (1,32),
        lista[1] not in range (1,13),
        lista[1] in [4,6,9,11] and lista[0]>30,
        bissexto == True and lista[1] == 2 and lista[0]>29,
        bissexto == False and lista[1] == 2 and lista[1]>28
                    ]

    if any(listaCondicoes):
        return 'A data não é válida.'
    else:
        return f'A sua data é {lista[0]} de {meses[lista[1]]} de {lista[2]}'

dataAlt = input('Escreva a data do seu aniversário no formato DD/MM/AAAA: ')
print(data(dataAlt))
