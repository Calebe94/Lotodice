inspect_args

check_dependencies

mkdir -p jogos/quina
mkdir -p jogos/mega

get_latest_quina_api()
{
    curl -s https://loteriascaixa-api.herokuapp.com/api/quina/latest
}

get_latest_mega_api()
{
    curl -s https://loteriascaixa-api.herokuapp.com/api/megasena/latest
}

get_latest_mega_contest()
{
    get_latest_mega_api | jq -r '.concurso'
}

get_latest_quina_contest()
{
    get_latest_quina_api | jq -r '.concurso'
}

get_latest_mega_game()
{
    find jogos/mega/ -iname "*-$(get_latest_mega_contest).csv" | sort -ur | head -n 1
}

get_latest_quina_game()
{
    find jogos/quina/ -iname "*-$(get_latest_quina_contest).csv" | sort -ur | head -n 1
}

get_latest_quina_dozens()
{
    get_latest_quina_api | jq -r '.dezenas[]' | awk '{printf "%s%s",sep,$0; sep=","}' | sed 's|\n||g'; print
}

get_latest_mega_dozens()
{
    get_latest_mega_api | jq -r '.dezenas[]' | awk '{printf "%s%s",sep,$0; sep=","}' | sed 's|\n||g'; print
}

check_latest_games()
{
    echo "Checking latest games..."
    echo "------------------------------------------"
    echo "Checking MEGA ..."
    echo "------------------------------------------"
    lotodice -c "$(get_latest_mega_game)" "$(get_latest_mega_dozens)"
    echo "------------------------------------------"
    echo "Checking QUINA ..."
    echo "------------------------------------------"
    lotodice -c "$(get_latest_quina_game)" "$(get_latest_quina_dozens)"
}

get_latest_mega_game
get_latest_quina_game
get_latest_quina_contest
get_latest_mega_contest
# check_latest_games
