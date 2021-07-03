
from datetime import datetime
from rich import print
data = datetime.now()
ano_atual = data.year
votos_dejoao = 0
votos_defelipe = 0
votos_demarcio = 0
nulos = 0
branco = 0
def autoriza_voto(nascimento):
    idade =ano_atual - nascimento
    if idade>=18 and idade<70:
        return 'OBRIGATÓRIO'
    elif 16<idade<18 or idade>70:
        return 'VOTO OPCIONAL'
    else:
        return 'VOTO NEGADO'
def votacao(autoriza,voto = 0):
    global votos_dejoao, votos_defelipe, votos_demarcio, nulos, branco
    if autoriza == 'VOTO NEGADO':
        return 'Você não pode votar'
    elif autoriza =='VOTO OPCIONAL' or autoriza =='OBRIGATÓRIO':
        if 1<=voto<=5:
            if voto == 1:
                votos_dejoao += 1
                return 'Voto computado'
            elif voto == 2:
                votos_defelipe += 1
                return 'Voto computado'
            elif voto == 3:
                votos_demarcio += 1
                return 'Voto computado'
            elif voto == 4:
                branco +=1
                return 'Voto computado'
            else:
                nulos+=1
                return 'Voto computado'
        else:
            return 'O número digitado é inválido'
    elif autoriza == 'fechar' and voto == 0:
        ganhador = ''
        total_ganhador =0
        votos_validos = votos_dejoao + votos_defelipe + votos_demarcio
        if votos_dejoao> votos_defelipe and votos_dejoao>votos_demarcio:
            ganhador = 'Joao'
            total_ganhador = votos_dejoao
        elif votos_defelipe> votos_dejoao and votos_defelipe>votos_demarcio:
            ganhador = 'Felipe'
            total_ganhador = votos_defelipe
        elif votos_demarcio> votos_dejoao and votos_demarcio>votos_defelipe:
            ganhador = 'Marcio'
            total_ganhador = votos_demarcio
        else:
            ganhador = 'Não houve ganhador nessa eleição'
        return f'''
        [yellow]-----------------------------------------------------
        -----------------------PREFEITO----------------------[/yellow]

        O total de votos válidos foi:[green] {votos_validos}[/green]
        O total de votos nulos foi: [green]{nulos}[/green]
        O total de votos brancos foi: [green]{branco}[/green]
        O prefeito eleito foi [green]{ganhador}[/green] com [green]{total_ganhador}[/green] votos

        [yellow]-----------------------------------------------------
        ------------------------------------------------------[/yellow]
        '''
while True:
    nascimento = autoriza_voto(int(input('Digite seu ano de nascimento: ')))
    voto = int(input('Digite o numero do seu candidato: '))
    print(votacao(nascimento,voto))
    terminar = input('Você deseja finalizar? [S/N]').upper()[0]
    if terminar == 'S':
        break
    else:
        continue        

print(votacao('fechar',0))
