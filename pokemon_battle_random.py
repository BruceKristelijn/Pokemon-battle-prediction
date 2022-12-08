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
    attacker.setLevel(random.randint(0, 99))

    # Get defender
    defender = get_pokemon(random.randint(0, len(POKEMONS)))
    defender.setLevel(random.randint(0, 99))

    battleresult = battle((attacker), (defender))
    results.append({
        'winner': battleresult.winner.Number,
        'loser':  battleresult.loser.Number,
        'winner_json': battleresult.winner.toJSON(),
        'loser_json': battleresult.loser.toJSON()
    })

    pass


# export results
with open('pokemon_sumulation.csv', 'w') as file:
    writer = csv.writer(file)

    writer.writerow(['winner', 'loser', 'winner_json', 'loser_json'])

    for result in results:
        writer.writerow([
            result['winner'], 
            result['loser'], 
            result['winner_json'],
            result['loser_json']
        ])