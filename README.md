# lotodice

`lotodice` é uma ferramenta em Python para gerar e verificar jogos da Mega Sena e Quina.

## Requisitos

- Python 3.x

## Instalação

Para instalar o `lotodice` basta rodar o seguinte comando:

```sh
pip install lotodice
```


### Instalando através do código fonte

Clone o repositório:

``` sh
git clone https://github.com/calebe94/lotodice
```

Entre no diretório criado:

``` sh
cd lotodice/
```

E rode o seguinte comando:

``` sh
pip install .
```

## Buildando o pacote

Se você está contribuindo com o projeto e vai testar a distribuição do pacote, siga os seguintes passos:

Com o repositório já clonado e no diretório raiz do projeto, crie um ambiente virtual Python:

```sh
virtualenv venv
source venv/bin/activate
```

Instale o pacote `build`:

```sh
pip install --upgrade build
```

Agora rode o comando a seguir na pasta raiz do projeto:

```sh
$ python3 -m build
```

Agora para instalar o `lotodice` através do pacote gerado, basta rodar o seguinte comando:

``` sh
pip install dist/lotodice_*.tar.gz
```

## Uso

```
lotodice -t [mega|quina] -q [quantidade] [--export caminho_para_arquivo.csv]
```

- `-t, --tipo`: Especifica o tipo de jogo (mega ou quina).
- `-q, --quantidade`: Especifica a quantidade de jogos a serem gerados.
- `-e, --export`: Exporta os jogos gerados para um arquivo CSV.

Para verificar se os jogos contidos em um arquivo CSV ganharam, use:

```
lotodice -c arquivo.csv "numeros_sorteados"
```

- `-c, --check`: Verifica se os jogos contidos no arquivo CSV ganharam, onde "numeros_sorteados" é uma string separada por vírgula com os números sorteados.

## Exemplos

Gerar 10 jogos da Mega Sena e imprimir no console:

```
lotodice -t mega -q 10
```

Exportar 20 jogos da Quina para um arquivo CSV:

```
lotodice -t quina -q 20 --export jogos_quina.csv
```

Verificar se os jogos contidos em `jogos_mega.csv` ganharam com os números sorteados `4,11,46,48,52`:

```
lotodice -c jogos_mega.csv "4,11,46,48,52"
```

## Licença

Este projeto está licenciado sob a [GPL3](./LICENSE).
