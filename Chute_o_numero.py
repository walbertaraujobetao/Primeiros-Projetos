# projeto 3 - Chute o número
# Objetivo: Criar um algorítimo que gera um valor aleatório, e o usuário tem que ir tentando
# até acertar o número gerado pelo computador!

import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        
    def GerarNumeroAleatorio(self):
        