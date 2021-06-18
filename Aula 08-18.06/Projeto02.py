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

tentativas = int(input('Quantas vezes você quer jogar? '))

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
    print(escolha)
    print("O computador escolheu: ")
    print(computer)
    if computer == rock and escolha == rock:
      print("Empatou")
    elif computer == scissors and escolha ==rock:
      print("Voce ganhou")
    else:
      print("Você perdeu")
  elif escolha == 2:
    escolha=paper
    print(escolha)
    print("O computador escolheu: ")
    print(computer)
    if computer == paper and escolha == paper:
      print("Empatou")
    elif computer==rock and escolha == paper:
      print("Voce ganhou")
    else:
      print("Você perdeu")
  else:
    escolha=scissors
    print(escolha)
    print("O computador escolheu: ")
    print(computer)
    if computer == scissors and escolha == scissors:
      print("Empatou")
    elif computer==paper and escolha == scissors:
      print("Voce ganhou")
    else:
      print("Você perdeu")
#computer



# print(rock[0:79])
