#!/usr/bin/env python3

import sys
import csv
import random

def gerar_jogo_quina():
    numeros = random.sample(range(1, 81), 5)
    numeros.sort()
    return numeros

def gerar_jogos_quina(qtde_jogos):
    jogos = []

    for _ in range(qtde_jogos):
        jogos.append(gerar_jogo_quina())

    return jogos

def verifica_tipo_premio(acertos=0):
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

def verificar_premio_quina(jogos, numeros_sorteados):
    for i, jogo in enumerate(jogos, start=1):
        acertos = set(jogo).intersection(numeros_sorteados)
        print(f"Jogo {i}: {', '.join(map(str, jogo))} - Acertos: {len(acertos)}")
        verifica_tipo_premio(len(acertos))

def carregar_jogos_quina(arquivo):
    jogos = []
    with open(arquivo, 'r') as csvfile:
        leitor = csv.reader(csvfile)
        for linha in leitor:
            jogo = [int(numero) for numero in linha]
            jogos.append(jogo)
    return jogos

def exportar_para_csv_quina(jogos, path):
    with open(path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for jogo in jogos:
            writer.writerow(jogo)

def main_quina():
    if len(sys.argv) != 4:
        print("Uso: python quina.py [quantidade_de_jogos | -export caminho_para_arquivo.csv | -check 'numeros_sorteados' caminho_para_arquivo.csv]")
        sys.exit(1)

    if sys.argv[1] == '-check':
        numeros_sorteados = list(map(int, sys.argv[2].split(',')))  # Remove aspas e converte para lista de inteiros
        arquivo_jogos = sys.argv[3]
        jogos = carregar_jogos_quina(arquivo_jogos)
        print(f"Números sorteados: {', '.join(map(str, numeros_sorteados))}")
        verificar_premio_quina(jogos, numeros_sorteados)

    elif sys.argv[1] == '-export':
        quantidade_de_jogos = int(sys.argv[3])
        resultados = gerar_jogos_quina(quantidade_de_jogos)
        caminho_arquivo = sys.argv[2]
        exportar_para_csv_quina(resultados, caminho_arquivo)
        print(f"Jogos exportados para {caminho_arquivo}")

    else:
        quantidade_de_jogos = int(sys.argv[1])
        resultados = gerar_jogos_quina(quantidade_de_jogos)
        for i, jogo in enumerate(resultados, start=1):
            print(f"Jogo {i}: {', '.join(map(str, jogo))}")

if __name__ == '__main__':
    main_quina()
