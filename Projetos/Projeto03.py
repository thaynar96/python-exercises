# Utilizando os conceitos aprendidos até dicionários, crie um programa onde 4
# jogadores joguem um dado e tenham resultados aleatórios.
# O programa tem que:
# • Perguntar quantas rodadas você quer fazer;X
# • Guardar os resultados dos dados em um dicionário.
# • Ordenar esse dicionário, sabendo que o vencedor tirou o maior número
# no dado.
# • Mostrar no final qual jogador ganhou mais rodadas e foi o grande
# campeão.
# Obs: O projeto deve ser feito individualmente e entregue até o final da aula 16

import random
from operator import itemgetter
from time import sleep
from rich.progress import track
from rich import print

jogador1=jogador2=jogador3=jogador4=empate=0
times = int(input('Número de rodadas:'))
for c in range(times):
    print(f'[green]Rodada {c+1}[/green]')
    jogadas = {
        'jogador 1':random.randint(1,6),
        'jogador 2':random.randint(1,6),
        'jogador 3':random.randint(1,6),
        'jogador 4':random.randint(1,6)
    }
    
    sorteio = []
    sorteio = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
    for i, d in enumerate(sorteio):
        print(f'[bold blue]{i+1}º lugar[/bold blue]: [yellow]{d[0]}[/yellow] com {d[1]}')
        sleep(1)
    
    if jogadas['jogador 1']> jogadas['jogador 2'] and jogadas['jogador 4']<jogadas['jogador 1']>jogadas['jogador 3']:
        jogador1 +=1
    elif jogadas['jogador 2']> jogadas['jogador 1'] and jogadas['jogador 4']<jogadas['jogador 2']>jogadas['jogador 3']:
        jogador2 +=1
    elif jogadas['jogador 3']> jogadas['jogador 2'] and jogadas['jogador 4']<jogadas['jogador 3']>jogadas['jogador 1']:
        jogador3 +=1
    elif jogadas['jogador 4']> jogadas['jogador 2'] and jogadas['jogador 3']<jogadas['jogador 4']>jogadas['jogador 1']:
        jogador4 +=1

    for c in range(5):
        sleep(0.3)
        print('∎',end=' ')
        sleep(0.3)
        print('□',end=' ')
    print()


for n in track(range(3), description="Carregando resultado..."):
    sleep(1)

if jogador1 == jogador2 and jogador2 ==jogador3 and jogador1==jogador4 and jogador4==jogador2 and jogador3==jogador4 and jogador3==jogador1:
        print('Ninguém ganhou')
elif jogador4<jogador1>jogador2 and jogador1>jogador3:
    print('[bold red]O jogador 1 ganhou[/bold red]:1st_place_medal:')
elif jogador4<jogador2>jogador1 and jogador2>jogador3:
    print('[bold red]O jogador 2 ganhou[/bold red]')
elif jogador4<jogador3>jogador2 and jogador3>jogador1:
    print('[bold red]O jogador 3 ganhou[/bold red]')
elif jogador3<jogador4>jogador2 and jogador4>jogador1:
    print('[bold red]O jogador 4 ganhou[/bold red]')
else:
    print('A quantidade de vitórias foi igual. Não há vencedores.')
