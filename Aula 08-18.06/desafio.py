# Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import sample

vezes_jogado = int(input('Quantos jogos você quer fazer?'))
lista = []
for c in range(vezes_jogado):
    print(sample(range(1, 60), 6))