from math import floor
from pokemon.pokemon import Pokemon
from pokemon.pokemontype import get_type_comparison
import random
import time


class Battleresult:
    winner: Pokemon
    loser: Pokemon

    def print(self):
        print("Pokemon battle winner: " + self.winner.Name)
        print("Loser: " + self.loser.Name)


# Calculates the potential damage a pokemon does against another pokemon.
def battle(pokemon1: Pokemon, pokemon2: Pokemon, log: bool = False) -> Battleresult:
    # Create class to return
    battleresult = Battleresult()

    pokemons = [pokemon1, pokemon2]
    pokemons = sorted(pokemons, key=lambda x: x.get_speed(), reverse=True)

    # Save temporary HP
    pokemons[0].TEMP_HP = pokemons[0].get_hp()
    pokemons[1].TEMP_HP = pokemons[1].get_hp()

    # Save the turn
    turn = 0

    while True:
        # Find the defender and attacker.
        attacker = turn % 2
        defender = 1 - turn % 2

        if log:
            print(pokemons[attacker].Name + " attacked " + pokemons[defender].Name)
            print(
                str(pokemons[defender].Name)
                + " HP is "
                + str(pokemons[defender].TEMP_HP)
            )
            time.sleep(3)

        # Attacker attack Defender
        damage = attack(pokemons[attacker], pokemons[defender])
        pokemons[defender].TEMP_HP -= damage

        if log:
            print(
                pokemons[attacker].Name
                + " did "
                + str(damage)
                + " damage. \n new hp is "
                + str(pokemons[defender].TEMP_HP)
            )

        # Check if any pokemon is dead
        if pokemons[0].TEMP_HP <= 0 or pokemons[1].TEMP_HP <= 0 or turn > 200:
            break

        # If not we continue and up the turn
        turn += 1

        if log:
            print("---")

    # Find winner by sorting with HP
    pokemons = sorted(pokemons, key=lambda x: x.TEMP_HP, reverse=True)

    # Delete temp values
    del pokemons[0].TEMP_HP
    del pokemons[1].TEMP_HP

    # fill winner
    battleresult.winner = pokemons[0]
    battleresult.loser = pokemons[1]

    return battleresult


# Calculates the potential damage a pokemon does against another pokemon.
def attack(attacker: Pokemon, defender: Pokemon):
    # Following the gen 1 formule where possible:
    # https://bulbapedia.bulbagarden.net/wiki/Damage#:~:text=Type2%5Ctimes%20random%7D-,where%3A,-Level%20is%20the

    # Start with 0 damage
    dmg = 0

    # Using 40 because it is the average of all the moves
    power = 40

    # Using 92 because it is the average of all the moves
    accuracy = 92

    # Same attack bonus will be 1 aswell.
    stab = 1.5

    # CriticalHit
    crit = 1
    randomNumber = random.uniform(1, 100)

    # Check if the number is less than or equal to 6.25
    if randomNumber <= 6.25:
        critical = 2

    # Compare type 1 and type 2
    type1 = get_type_comparison(attacker.Type1, defender.Type1)

    # Compare type 2 but make sure type2 is correct other wise type2 stays 1.
    type2 = 1
    if attacker.Type2 != "none" and defender.Type2 != "none":
        type2 = get_type_comparison(attacker.Type2, defender.Type2)

    # Calculate attack / defence
    ad = attacker.get_attack() / defender.get_defense()

    # Left side of formula
    dmg = (
        (
            (((2 * attacker.Level * crit) / 5) + 2)
            * power
            * attacker.get_attack()
            / defender.get_defense()
        )
        / 50
    ) + 2

    # Right side of formula
    dmg *= stab * type1 * type2

    randomNumber = random.uniform(1, 100)
    if randomNumber <= accuracy:
        return floor(dmg)
    else:
        return 0


# Used to get the type so type2 is comparable.
def getType2(pokemon: Pokemon):
    if pokemon.Type2 == "none":
        return pokemon.Type1
    else:
        return pokemon.Type1
