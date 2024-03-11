# echo "# this file is located in 'src/new_command.sh'"
# echo "# code for 'lotodice new' goes here"
# echo "# you can edit it freely and regenerate (it will not be overwritten)"
inspect_args

check_dependencies

games=5

mkdir -p jogos/quina
mkdir -p jogos/mega

get_quina_latest_context()
{
    curl -s https://loteriascaixa-api.herokuapp.com/api/quina/latest | jq '.proximoConcurso'
}

get_mega_latest_context()
{
    curl -s https://loteriascaixa-api.herokuapp.com/api/megasena/latest | jq '.proximoConcurso'
}

create_new_games()
{
    echo "Creating new games..."
    lotodice -t mega -q "$games" -e jogos/mega/"$(date +%F)"-"$(get_mega_latest_context)".csv
    lotodice -t quina -q "$games" -e jogos/quina/"$(date +%F)"-"$(get_quina_latest_context)".csv

    lotodice -b jogos/mega/"$(date +%F)"-"$(get_mega_latest_context)".csv jogos/quina/"$(date +%F)"-"$(get_quina_latest_context)".csv
}

create_new_games
