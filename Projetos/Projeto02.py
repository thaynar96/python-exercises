# Utilizando os conceitos aprendidos até estruturas de repetição, crie um
# programa que jogue pedra, papel e tesoura (Jokenpô) com você.
# O programa tem que:
# • Permitir que eu decida quantas rodadas iremos fazer;
# • Ler a minha escolha (Pedra, papel ou tesoura);
# • Decidir de forma aleatória a decisão do computador;
# • Mostrar quantas rodadas cada jogador ganhou;
# • Determinar quem foi o grande campeão de acordo com a quantidade de
# vitórias de cada um (computador e jogador);
# • Perguntar se o Jogador quer jogar novamente, se sim inicie volte a escolha
# de quantidade de rodadas, se não finalize o programa.
# Obs: O projeto deve ser feito individualme
# nte e entregue até o final da aula 11.
import random
import os
os.system('cls')
from time import sleep
from rich import print

tentativas = int(input('Quantas vezes você quer jogar? '))

while True:
  empate = 0
  venceu_computador = 0
  venceu_jogador = 0
  for vezes in range(tentativas):
      rock = '''
          _______
      ---'   ____)
            (_____)
            (_____)
            (____)
      ---.__(___)
      '''

      paper = '''
          _______
      ---'   ____)____
                ______)
                _______)
              _______)
      ---.__________)
      '''

      scissors = '''
          _______
      ---'   ____)____
                ______)
            __________)
            (____)
      ---.__(___)
      '''
      escolha = int(input("Escreva 1 para pedra, 2 para papel e 3 para tesoura: "))
      while not (1<=escolha<=3):
        escolha = int(input("Comando inválido. Escolha entre 1,2 e 3: "))
      options = [rock,paper,scissors]
      computer= random.choice(options)
      if escolha ==1:
        escolha = rock
        print(f'Você escolheu:\n[blue]{escolha}[/blue]')
        print(f"O computador escolheu:",end=' ')
        for i in range(5):
          print('.', end=' ')
          sleep(0.3)
        print(f'[green]{computer}[/green]')
      #Quando a escolha for pedra
        if computer == rock and escolha == rock:
          print("Empatou")
          empate += 1
        elif computer == scissors and escolha ==rock:
          print("Voce ganhou")
          venceu_jogador += 1
        else:
          print("Você perdeu")
          venceu_computador += 1
      #Quando a escolha for papel
      elif escolha == 2:
        escolha=paper
        print(f'Você escolheu:\n[blue]{escolha}[/blue]')
        print(f"O computador escolheu:",end=' ')
        for i in range(5):
          print('.', end=' ')
          sleep(0.3)
        print(f'[green]{computer}[/green]')
        if computer == paper and escolha == paper:
          print("Empatou")
          empate += 1
        elif computer==rock and escolha == paper:
          print("Voce ganhou")
          venceu_jogador +=1
        else:
          print("Você perdeu")
          venceu_computador +=1 
        #Quando a escolha for tesoura
      else:
        escolha=scissors
        print(f'Você escolheu:\n[blue]{escolha}[/blue]')
        print(f"O computador escolheu:",end=' ')
        for i in range(5):
          print('.', end=' ')
          sleep(0.3)
        print(f'[green]{computer}[/green]')
        if computer == scissors and escolha == scissors:
          print("Empatou")
          empate +=1
        elif computer==paper and escolha == scissors:
          print("Voce ganhou")
          venceu_jogador +=1
        else:
          print("Você perdeu")
          venceu_computador +=1
  # print(empate,venceu_computador,venceu_jogador) teste de valores
  print()
  print()
  print('Calculando resultado: ')
  for i in range(6):
          print('.',end=' ')
          sleep(1)
  if empate > venceu_computador and empate>venceu_jogador:
    print( f'''\n[yellow]
  ╔═════════════╗
  ║Você empatou!║ 
  ╚═════════════╝[/yellow]
Você empatou com o computador. O computador teve {venceu_computador} vitórias e você {venceu_jogador} vitórias. ''')
  elif venceu_computador> empate and venceu_computador>venceu_jogador:
    print(f'''\n [yellow]
    ╔═════════════╗
    ║ Você perdeu!║ 
    ╚═════════════╝ [/yellow]        
O computador teve {venceu_computador} vitórias e você {venceu_jogador} vitórias. :slightly_frowning_face:''')
  elif venceu_jogador> empate and venceu_jogador>venceu_computador or venceu_jogador== empate:
    print(f'''\n [yellow]
╔═════════════╗
║ Você ganhou!║ 
╚═════════════╝[/yellow]
O computador teve {venceu_computador} vitórias e você {venceu_jogador} vitórias. :1st_place_medal:''')
  elif venceu_jogador == venceu_computador:
    print(f'''\n[yellow]
    ╔═════════════╗
    ║Você empatou!║ 
    ╚═════════════╝[/yellow]
O computador teve {venceu_computador} vitórias e você {venceu_jogador} vitórias. :upside-down_face:''')
  final = input('Você quer continuar jogando? S/N :').upper().strip()[0]
  if final == 'S':
    continue
  else:
    break
