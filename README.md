# Gerador de Jogos da Mega Sena e Quina

Este é um script em Python para gerar e verificar jogos da Mega Sena e Quina.

## Requisitos

- Python 3.x

## Uso

```
python main.py -t [mega|quina] -q [quantidade] [--export caminho_para_arquivo.csv]
```

- `-t, --tipo`: Especifica o tipo de jogo (mega ou quina).
- `-q, --quantidade`: Especifica a quantidade de jogos a serem gerados.
- `-e, --export`: Exporta os jogos gerados para um arquivo CSV.

Para verificar se os jogos contidos em um arquivo CSV ganharam, use:

```
python main.py -c arquivo.csv "numeros_sorteados"
```

- `-c, --check`: Verifica se os jogos contidos no arquivo CSV ganharam, onde "numeros_sorteados" é uma string separada por vírgula com os números sorteados.

## Exemplos

Gerar 10 jogos da Mega Sena e imprimir no console:

```
python main.py -t mega -q 10
```

Exportar 20 jogos da Quina para um arquivo CSV:

```
python main.py -t quina -q 20 --export jogos_quina.csv
```

Verificar se os jogos contidos em `jogos_mega.csv` ganharam com os números sorteados `4,11,46,48,52`:

```
python main.py -c jogos_mega.csv "4,11,46,48,52"
```

## Licença

Este projeto está licenciado sob a [GPL3](./LICENSE).
