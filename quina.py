from jogo import Jogo

class Quina(Jogo):
    def __init__(self, numeros_sorteados):
        super().__init__(80, numeros_sorteados)
        self.quantidade_numeros = 5

    def verifica_tipo_premio(self, acertos=0):
        if acertos == 2:
            print("---------------------")
            print("ACERTAMO UM DUQUE!!!")
            print("---------------------")
        elif acertos == 3:
            print("---------------------")
            print("ACERTAMO UM TERNO!!!")
            print("---------------------")
        elif acertos == 4:
            print("--------------------")
            print("ACERTAMO A QUADRA!!!")
            print("--------------------")
        elif acertos == 5:
            print("----------------------------")
            print("GANHAMOOOOOO CARALHOOOOOW!!!")
            print("----------------------------")
        else:
            pass
