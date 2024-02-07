#!/usr/bin/env python3
import argparse
from .jogo import Jogo
from .mega import MegaSena
from .quina import Quina

def main():
    parser = argparse.ArgumentParser(description="Jogos da Mega Sena ou Quina")
    parser.add_argument("-t", "--tipo", choices=["mega", "quina"], help="Tipo de jogo (mega ou quina)")
    parser.add_argument("-q", "--quantidade", type=int, help="Quantidade de jogos a serem gerados")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--export", metavar="caminho_para_arquivo.csv", help="Exporta os jogos para um arquivo CSV")
    group.add_argument("-c", "--check", nargs=2, metavar=("arquivo.csv", "numeros_sorteados"), help="Verifica se os jogos contidos no arquivo CSV ganharam")

    args = parser.parse_args()

    if args.check:
        arquivo, numeros_sorteados = args.check
        numeros_sorteados = list(map(int, numeros_sorteados.split(',')))
        jogo = MegaSena(numeros_sorteados) if args.tipo == 'mega' else Quina(numeros_sorteados)
        jogos = jogo.carregar_jogos(arquivo)
        print(f"Números sorteados: {', '.join(map(str, numeros_sorteados))}")
        jogo.verificar_premio(jogos)
    elif args.quantidade and args.tipo:
        jogo = MegaSena([]) if args.tipo == 'mega' else Quina([])
        resultados = jogo.gerar_jogos(args.quantidade)
        if args.export:
            jogo.exportar_para_csv(resultados, args.export)
            print(f"Jogos exportados para {args.export}")
        else:
            for i, jogo in enumerate(resultados, start=1):
                print(f"Jogo {i}: {', '.join(map(str, jogo))}")
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
