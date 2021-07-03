# class Pessoa:
#     def __init__(self,nome,idade,peso):
#         self.nomePessoa = nome
#         self.idadePessoa = idade
#         self.pesoPessoa = peso
    
#     def comer(self,calorias):
#         if self.idadePessoa>30:
#             self.pesoPessoa += (calorias *2)
#         else:
#             self.pesoPessoa += calorias
#         return self.pesoPessoa
    
#     def malhar(self,calorias):
#         if self.idadePessoa<30:
#             self.pesoPessoa -= (calorias*2)
#         else:
#             self.pesoPessoa -= calorias
#         return self.pesoPessoa
    

# pessoa1 = Pessoa('Thaynar',24,68.0)
# pessoa2 = Pessoa('João',35,60)


# print(pessoa1.comer(5))
# print(pessoa2.comer(5))
# print(pessoa1.malhar(5))

#Crie uma classe chamada Conta para simular as operações de uma conta corrente. Sua classe deverá ter os atributos Titular e Saldo, e os métodos Sacar e Depositar. Crie um objeto da classe Conta e teste os atributos e métodos implementados.​ Adicione uma regra no método Sacar, onde o usuário só poderá sacar se o Saldo for maior que zero, caso contrário mostre a mensagem na tela: "Você não tem saldo suficiente para essa operação."

class Conta:
    def __init__(self,Titular,Saldo):
        self.nome_titular = Titular
        self.saldo_conta=Saldo
    
    def sacar(self,saque):
        if self.saldo_conta>0:
            self.saldo_conta -= saque
            return self.saldo_conta
        else:
            return 'Você não tem saldo suficiente para essa operação.'
        
    
    def depositar(self,deposito):
        self.saldo_conta += deposito
    

titular1 = Conta('Joao',1000000)
titular2 = Conta('Joaquim',30)

print(titular1.sacar(100))
print(titular1.sacar(100))