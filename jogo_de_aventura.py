# Um jogo de decisões onde eu terei que criar vários finais diferentes baseados nas respostas que foram dadas!

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no norte ou no sul? (n/s) '
        self.pergunta2 = 'Você prefere a espada ou o escudo? (espada/escudo) '
        self.pergunta3 = 'Qual é a sua especialidade? (linda de frente/tatico) '
        self.finalHistoria1 = 'Você será um heroi na linha de frente!' 
        self.finalHistoria2 = 'Você será um heroi protegendo todas as nossas tropas!'
        self.finalHistoria3 = 'Você irá se sacrificar nas batalha!'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha!'
        
    def Iniciar(self):
        # layout
        
        # criar as janelas
        # fazer algo com os dados
        resposta1 = input(self.pergunta1)
        if resposta1 == 'n':
            resposta1B = input(self.pergunta2)
            if resposta1B == 'espada':
                print(self.finalHistoria1)
            if resposta1B == 'escudo':
                print(self.finalHistoria2)
        if resposta1 == 's':
            resposta1B = input(self.pergunta3)
            if resposta1B == 'linha de frente':
                print(self.finalHistoria3)
            if resposta1B == 'tatico':
                print(self.finalHistoria4)
                
                
jogo = JogoDeAventura()
jogo.Iniciar()