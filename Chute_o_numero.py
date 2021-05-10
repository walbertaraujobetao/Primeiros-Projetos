# projeto 3 - Chute o número
# Objetivo: Criar um algorítimo que gera um valor aleatório, e o usuário tem que ir tentando
# até acertar o número gerado pelo computador!

import random
import PySimpleGUI as sg 


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
        
    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Seu Palpite', size=(40,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(40,10))]
        ]
        # criar uma janela
        self.janela = sg.Window('Seu Palpite', layout=layout) # cuidar com letras com maiúsculas!!!
        self.GerarNumeroAleatorio()
        try: # no final sempre lembrar de tratar os erros
            while True:
                # receber valores
                self.evento, self.valores = self.janela.Read()
                # depois fazer alguma coisa com esses valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Errou! Digite um número menor!')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Errou! Digite um número maior!')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Você Acertou!')
                            break
                        
                        
        except:
            print('Digite somente números!')
            self.Iniciar()
                    
    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')
        
        
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)
        
        
chute = ChuteONumero() # Lembrar sempre de chamar (instanciar) a classe!!!
chute.Iniciar()