#!/usr/bin/env python3
import sys
import csv
import random
from jogo import Jogo
from mega import MegaSena
from quina import Quina

def main():
    if len(sys.argv) < 4:
        print("Uso: python nome_do_arquivo.py [tipo_de_jogo (mega/quina) | quantidade_de_jogos | -export caminho_para_arquivo.csv | -check 'numeros_sorteados' caminho_para_arquivo.csv]")
        sys.exit(1)

    tipo_de_jogo = sys.argv[1]

    if tipo_de_jogo not in ['mega', 'quina']:
        print("Tipo de jogo inválido. Use 'mega' ou 'quina'.")
        sys.exit(1)

    numeros_sorteados = list(map(int, sys.argv[2].split(',')))
    arquivo = sys.argv[-1]

    if sys.argv[3] == '-check':
        jogo = MegaSena(numeros_sorteados) if tipo_de_jogo == 'mega' else Quina(numeros_sorteados)
        jogos = jogo.carregar_jogos(arquivo)
        print(f"Números sorteados: {', '.join(map(str, numeros_sorteados))}")
        jogo.verificar_premio(jogos)

    elif sys.argv[3] == '-export':
        quantidade_de_jogos = int(sys.argv[2])
        jogo = MegaSena(numeros_sorteados) if tipo_de_jogo == 'mega' else Quina(numeros_sorteados)
        resultados = jogo.gerar_jogos(quantidade_de_jogos)
        jogo.exportar_para_csv(resultados, arquivo)
        print(f"Jogos exportados para {arquivo}")

    else:
        quantidade_de_jogos = int(sys.argv[2])
        jogo = MegaSena(numeros_sorteados) if tipo_de_jogo == 'mega' else Quina(numeros_sorteados)
        resultados = jogo.gerar_jogos(quantidade_de_jogos)
        for i, jogo in enumerate(resultados, start=1):
            print(f"Jogo {i}: {', '.join(map(str, jogo))}")

if __name__ == '__main__':
    main()
