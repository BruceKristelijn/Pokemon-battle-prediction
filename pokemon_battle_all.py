from pokemon.pokemon import get_pokemon
from pokemon.battle import battle

import csv

# Get mewtwo

allpokemon = get_pokemon()
results = []

# simulate

print("Simulating all pokemon, length: " + str(len(allpokemon) * len(allpokemon)))

for pokemon in allpokemon:
    print("Simulating " + pokemon.Name + " [" + str(pokemon.Number) + "]")

    wins = 0
    for enemypokemon in allpokemon:
        if(enemypokemon != pokemon):
            if(battle(pokemon, enemypokemon).winner == pokemon):
                wins += 1
    results.append({'wins': wins, 'info': pokemon})
    print("Done, " + pokemon.Name +" wins: " + str(wins) + ". Left: " + str(len(allpokemon) - pokemon.Number))

# export results
with open('pokemon_battle_all.csv', 'w') as file:
    writer = csv.writer(file)

    writer.writerow(['number', 'name', 'wins', 'type', 'attack'])

    for result in results:
        writer.writerow([
            result['info'].Number, 
            result['info'].Name, 
            result['wins'],
            result['info'].Type1,
            result['info'].source.Attack,
        ])