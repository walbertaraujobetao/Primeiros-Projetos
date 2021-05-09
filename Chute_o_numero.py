# projeto 3 - Chute o número
# Objetivo: Criar um algorítimo que gera um valor aleatório, e o usuário tem que ir tentando
# até acertar o número gerado pelo computador!

import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
        
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.tentar_novamente == True:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print('Errou! Digite um número menor!')
                self.PedirValorAleatorio()
            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print('Errou! Digite um número maior!')
                self.PedirValorAleatorio()
            if int(self.valor_do_chute) == self.valor_aleatorio:
                self.tentar_novamente = False
                print('Você Acertou!')
        
    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')
        
        
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)
        
        
chute = ChuteONumero() # Lembrar sempre de chamar (instanciar) a classe!!!
chute.Iniciar()