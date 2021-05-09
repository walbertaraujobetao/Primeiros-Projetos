# simular o valor de um dado, gerando um valor de 1 à 6
import random
import PySimpleGUI


class SimuladorDeDado:
    def __init__(self):  # definindo o comportamento inicial desta classe
        self.valor_minimo = 1  # declarando valor minimo
        self.valor_maximo = 6  # declarendo valor máximo
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado: '
        # layout
        layout = [
            []

        ]
        # Criar uma janela
        # ler os valores da tela
        # fazer alguma coisa com esses valores

    def Iniciar(self):  # criando método para iniciar
        resposta = input(self.mensagem)  # vamos guar a resposta do usuário com um input
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()  # sempre criar um método com nome simples, para ficar de fácil compreensão
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar: Sim ou não!')
        except:
            print('Ocorreu um erro ao receber sua resposta!')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))  # chamar a função d o random para ser impressa


simulador = SimuladorDeDado()  # sempre tem que ser inicializado
simulador.Iniciar()
