# Um jogo de decisões onde eu terei que criar vários finais diferentes baseados nas respostas que foram dadas!

import PySimpleGUI as sg

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (n/s) '
        self.pergunta2 = 'Você prefere a espada ou o escudo? (espada/escudo) '
        self.pergunta3 = 'Qual é a sua especialidade? (linha de frente/tatico) '
        self.finalHistoria1 = 'Você será um heroi na linha de frente!' 
        self.finalHistoria2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar nas batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'
        
    def Iniciar(self):
        # layout
        layout = [
            [sg.Output(size=(50,0))],
            [sg.Input(size=(30,0),key='escolha')],
            [sg.Button('iniciar'), sg.Button('Responder')],
        ]
        # criar as janelas
        self.janela = sg.Window('Jogo de Aventura', layout=layout)
        while True:
            # ler os dados
            self.LerValores()
            # fazer algo com os dados
            print(self.pergunta1)
            self.LerValores()
            if self.valores['escolha'] == 'n':
                print(self.pergunta2)
                self.LerValores()
                if self.valores['escolha'] == 'espada':
                    print(self.finalHistoria1)
                if self.valores['escolha'] == 'escudo':
                    print(self.finalHistoria2)
            if self.valores['escolha'] == 's':
                print(self.pergunta3)
                self.LerValores()
                if self.valores['escolha'] == 'linha de frente':
                    print(self.finalHistoria3)
                if self.valores['escolha'] == 'tatico':
                    print(self.finalHistoria4)
    
    def LerValores(self):
        self.evento, self.valores = self.janela.Read()
                
jogo = JogoDeAventura()
jogo.Iniciar()
                
