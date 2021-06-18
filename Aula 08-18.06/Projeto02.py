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
      options = [rock,paper,scissors]
      computer= random.choice(options)
      if escolha ==1:
        escolha= rock
        print(f'[blue]{escolha}[/blue]')
        print( "O computador escolheu: ")
        print(f'[red]{computer}[/red]')
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
        print(f'[blue]{escolha}[/blue]')
        print("O computador escolheu: ")
        print(f'[red]{computer}[/red]')
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
        print(f'[blue]{escolha}[/blue]')
        print("O computador escolheu: ")
        print(f'[red]{computer}[/red]')
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
  if empate > venceu_computador and empate>venceu_jogador:
    print( f'Você empatou com o computador. O computador teve {venceu_computador} vitórias e você {venceu_jogador} vitórias. ')

  elif venceu_computador> empate and venceu_computador>venceu_jogador or venceu_computador== empate:
    print(f'Você perdeu. O computador teve {venceu_computador} vitórias e você {venceu_jogador} vitórias. :slightly_frowning_face:')

  elif venceu_jogador> empate and venceu_jogador>venceu_computador or venceu_jogador== empate:
    print(f'Você ganhou. O computador teve {venceu_computador} vitórias e você {venceu_jogador} vitórias. :1st_place_medal:')

  elif venceu_jogador == venceu_computador:
    print(f'Você empatou. O computador teve {venceu_computador} vitórias e você {venceu_jogador} vitórias. :upside-down_face:')
  final = input('Você quer continuar jogando? S/N :').upper().strip()[0]
  if final == 'S':
    continue
  else:
    break
