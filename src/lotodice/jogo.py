import csv
import random


class Jogo:
    def __init__(self, range_max, numeros_sorteados):
        self.range_max = range_max
        self.numeros_sorteados = numeros_sorteados

    def gerar_jogo(self):
        numeros = random.sample(
            range(1, self.range_max + 1), self.quantidade_numeros
        )  # noqa
        numeros.sort()
        return numeros

    def gerar_jogos(self, qtde_jogos):
        jogos = []

        for _ in range(qtde_jogos):
            jogos.append(self.gerar_jogo())

        return jogos

    def verificar_premio(self, jogos):
        for i, jogo in enumerate(jogos, start=1):
            acertos = set(jogo).intersection(self.numeros_sorteados)
            print(
                f"Jogo {i}: {', '.join(map(str, jogo))} - Acertos: {len(acertos)}"
            )  # noqa
            self.verifica_tipo_premio(len(acertos))

    def carregar_jogos(self, arquivo):
        jogos = []
        with open(arquivo, "r") as csvfile:
            leitor = csv.reader(csvfile)
            for linha in leitor:
                jogo = [int(numero) for numero in linha]
                jogos.append(jogo)
        return jogos

    def exportar_para_csv(self, jogos, path):
        with open(path, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            for jogo in jogos:
                writer.writerow(jogo)
