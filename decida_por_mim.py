# Faça uma pergunta para o programa e ele teráque te dar uma resposta!

import random
import PySimpleGUI as sg
from time import sleep

class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe!',
            'Não faz isso não!',
            'Acho que está na hora certa!',
            'Talvez...'
        ]
    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Faça sua pergunta: ')],
            [sg.Input()],
            [sg.Output(size=(20,10))],
            [sg.Button('Decida por mim!')]
        ]
        # Criar janela
        self.janela = sg.Window('Decida por mim!', layout=layout)
        # Ler os valores
        self.eventos, self.valores = self.janela.Read()
        # Fazer algo com so valores
        if self.eventos == 'Decida por mim!':
            print(random.choice(self.respostas))
            sleep(3)
        self.janela.Close()

decida = DecidaPorMim()
decida.Iniciar()
