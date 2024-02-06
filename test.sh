#!/bin/bash

# Verifica se os argumentos foram fornecidos corretamente
if [ "$#" -ne 3 ]; then
    echo "Uso: $0 'numeros_quina' 'numeros_mega' quantidade_de_jogos"
    exit 1
fi

numeros_quina=$1
numeros_mega=$2
qtde_jogos=$3

index=1

mkdir -p teste/

# Loop para gerar jogos até que haja um prêmio
while true; do
    # Gera jogos para a Quina
    python quina.py -export teste/teste-quina-$index.csv $qtde_jogos
    # Gera jogos para a Mega Sena
    python mega.py -export teste/teste-mega-$index.csv $qtde_jogos

    # Verifica os jogos gerados
    resultado_quina=$(python quina.py -check "$numeros_quina" teste/teste-quina-$index.csv)
    resultado_mega=$(python mega.py -check "$numeros_mega" teste/teste-mega-$index.csv)

    # Verifica se houve um prêmio na Quina ou na Mega Sena
    if [[ $resultado_quina == *"GANHAMOOOOOO CARALHOOOOOW!!!"* ]] || [[ $resultado_mega == *"GANHAMOOOOOO CARALHOOOOOW!!!"* ]]; then
        echo "Prêmio encontrado na rodada $index!"
        break
    fi
    # Verifica se houve algum outro prêmio
    # Quina
    if [[ $resultado_mega == *"ACERTAMO A QUADRA!!!"* ]]; then
        echo "Quina encontrada na rodada $index!" | tee -a quinas.log
    fi

    # Quadra
    if [[ $resultado_quina == *"ACERTAMO A QUADRA!!!"* ]] || [[ $resultado_mega == *"ACERTAMO A QUADRA!!!"* ]]; then
        echo "Quadra encontrada na rodada $index!" | tee -a quadras.log
    fi

    # Terno
    if [[ $resultado_quina == *"ACERTAMO UM TERNO!!!"* ]]; then
        echo "Terno encontrada na rodada $index!" | tee -a ternos.log
    fi

    # Duque
    if [[ $resultado_quina == *"ACERTAMO UM DUQUE!!!"* ]]; then
        echo "Duque encontrado na rodada $index!" | tee -a duques.log
    fi


    index=$((index + 1))
done

echo "Fim do script."
