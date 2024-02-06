from .jogo import Jogo

class MegaSena(Jogo):
    def __init__(self, numeros_sorteados):
        super().__init__(60, numeros_sorteados)
        self.quantidade_numeros = 6

    def verifica_tipo_premio(self, acertos=0):
        if acertos == 4:
            print("--------------------")
            print("ACERTAMO A QUADRA!!!")
            print("--------------------")
        elif acertos == 5:
            print("-------------------")
            print("ACERTAMO A QUINA!!!")
            print("-------------------")
        elif acertos == 6:
            print("----------------------------")
            print("GANHAMOOOOOO CARALHOOOOOW!!!")
            print("----------------------------")
        else:
            pass
