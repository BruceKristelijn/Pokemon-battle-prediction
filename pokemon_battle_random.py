from pokemon.pokemon import get_pokemon
from pokemon.battle import battle

from tqdm import tqdm

import random
import json
import csv

# Create constants
POKEMONS = get_pokemon()

# Create amount of simulations to prepare.
print("How many simulations do you want to run?")
COUNT = int(input())


# Create results
results = []

# Simulate
print("Randomizing simulation of all pokemon, length: " + str(COUNT))

for i in tqdm(range(0, COUNT)):
    # Get attacker
    attacker = get_pokemon(random.randint(0, len(POKEMONS)))
    attacker.setLevel(random.randint(1, 99))

    # Get defender
    defender = get_pokemon(random.randint(0, len(POKEMONS)))
    defender.setLevel(random.randint(1, 99))

    battleresult = battle((attacker), (defender))
    results.append({
        'winner': battleresult.winner,
        'loser':  battleresult.loser
    })

    pass


# export results
with open('pokemon_simulation.csv', 'w') as file:
    writer = csv.writer(file)

    writer.writerow(['winner_level', 'winner_hp', 'winner_attack', 'winner_defense', 'winner_speed', 'winner_type', 
                    'loser_level', 'loser_hp', 'loser_attack', 'loser_defense', 'loser_speed', 'loser_type'])

    for result in results:
        writer.writerow([result['winner'].Level, result['winner'].get_hp(),  result['winner'].get_attack(), result['winner'].get_defense(), result['winner'].get_speed(), result['winner'].Type1,result['loser'].Level, result['loser'].get_hp(),  result['loser'].get_attack(), result['loser'].get_defense(), result['loser'].get_speed(), result['loser'].Type1])