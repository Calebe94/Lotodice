#!/usr/bin/env python3
import argparse

from .browser import browser
from .mega import MegaSena
from .quina import Quina


def parse_browser_args(browser_args):
    """Parses the browser arguments into a dictionary."""
    parsed_args = {}
    for arg in browser_args:
        if "=" not in arg:
            raise argparse.ArgumentTypeError(
                f"Formato inválido: '{arg}'."
                "Use o formato tipo=/caminho/para/arquivo.csv"
            )
        key, value = arg.split("=", 1)
        if key not in ["mega", "quina"]:
            raise argparse.ArgumentTypeError(
                f"Tipo inválido: '{key}'."
                "Somente 'mega' e 'quina' são permitidos."  # noqa
            )
        parsed_args[key] = value
    return parsed_args


def main():
    parser = argparse.ArgumentParser(description="Jogos da Mega Sena ou Quina")
    parser.add_argument(
        "-t",
        "--tipo",
        choices=["mega", "quina"],
        help="Tipo de jogo (mega ou quina)",  # noqa
    )
    parser.add_argument(
        "-q",
        "--quantidade",
        type=int,
        help="Quantidade de jogos a serem gerados",  # noqa
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-e",
        "--export",
        metavar="caminho_para_arquivo.csv",
        help="Exporta os jogos para um arquivo CSV",
    )
    group.add_argument(
        "-c",
        "--check",
        nargs=2,
        metavar=("arquivo.csv", "numeros_sorteados"),
        help="Verifica se os jogos contidos no arquivo CSV ganharam",
    )
    group.add_argument(
        "-b",
        "--browser",
        nargs="+",
        metavar="tipo=/path/to/file.csv",
        help="Faz os jogos no site da Loterias Caixa (ex.: mega=/path/to/file.csv quina=/path/to/file.csv)",  # noqa
    )

    args = parser.parse_args()

    if args.check:
        arquivo, numeros_sorteados = args.check
        numeros_sorteados = list(map(int, numeros_sorteados.split(",")))
        jogo = (
            MegaSena(numeros_sorteados)
            if args.tipo == "mega"
            else Quina(numeros_sorteados)
        )
        jogos = jogo.carregar_jogos(arquivo)
        print(f"Números sorteados: {', '.join(map(str, numeros_sorteados))}")
        jogo.verificar_premio(jogos)

    elif args.browser:
        # Parseando os argumentos do navegador
        browser_args = parse_browser_args(args.browser)
        mega_path = browser_args.get("mega")
        quina_path = browser_args.get("quina")

        if not mega_path:
            print(
                "Erro: O arquivo de jogos da Mega Sena é obrigatório para o modo browser."  # noqa
            )
        else:
            browser(mega_path, quina_path)

    elif args.quantidade and args.tipo:
        jogo = MegaSena([]) if args.tipo == "mega" else Quina([])
        resultados = jogo.gerar_jogos(args.quantidade)
        if args.export:
            jogo.exportar_para_csv(resultados, args.export)
            print(f"Jogos exportados para {args.export}")
        else:
            for i, jogo in enumerate(resultados, start=1):
                print(f"Jogo {i}: {', '.join(map(str, jogo))}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
