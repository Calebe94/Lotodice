#!/usr/bin/env sh

[ -z "$LOTODICE_PATH" ] && LOTODICE_PATH=~/Projects/mega-sena/

games=5

cd "$LOTODICE_PATH" > /dev/null || exit 1

. venv/bin/activate

get_latest_games()
{
    latest_mega="$(find jogos/ -iname "mega*.csv" | sort -ur | head -n 1)"
    latest_quina="$(find jogos/ -iname "quina*.csv" | sort -ur | head -n 1)"
    echo "Checking latest games..."
    echo "------------------------------------------"
    echo "Checking QUINA: $latest_quina ..."
    echo "------------------------------------------"
    lotodice -c "$latest_quina" "$(curl -s https://loteriascaixa-api.herokuapp.com/api/quina/latest | jq -r '.dezenas[]' | awk '{printf "%s%s",sep,$0; sep=","}' | sed 's|\n||g'; print)"
    echo "----------------------------------------"
    echo "Checking MEGA: $latest_mega ..."
    echo "----------------------------------------"
    lotodice -c "$latest_mega" "$(curl -s https://loteriascaixa-api.herokuapp.com/api/megasena/latest | jq -r '.dezenas[]' | awk '{printf "%s%s",sep,$0; sep=","}' | sed 's|\n||g'; print)"
}

create_new_games()
{
    echo "Creating new games..."
    lotodice -t mega -q "$games" -e jogos/mega-"$(date +%F)".csv
    lotodice -t quina -q "$games" -e jogos/quina-"$(date +%F)".csv

    lotodice -b jogos/mega-"$(date +%F)".csv jogos/quina-"$(date +%F)".csv
}

main()
{
    case "$1" in
        "check") get_latest_games ;;
        *)
            games="$1"
            create_new_games
            ;;
    esac
}

main "$@"

cd - > /dev/null || exit 1
