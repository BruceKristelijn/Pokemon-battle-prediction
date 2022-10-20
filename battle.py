from pokemon import Pokemon
from pokemontype import GetComparison


class Battleresult:
    pokemon1: Pokemon
    pokemon2: Pokemon
    attack1: float
    attack2: float
    winner: Pokemon
    loser: Pokemon

    def print(self):
        print("Pokemon battle winner: " + self.winner.Name)
        print("Loser: " + self.loser.Name)
        print("Attack 1 (" + self.pokemon1.Name + "): " + str(self.attack1))
        print("Attack 2 (" + self.pokemon2.Name + "): " + str(self.attack2))


# Calculates the potential damage a pokemon does against another pokemon.
def battle(pokemon1: Pokemon, pokemon2: Pokemon) -> Battleresult:
    # Create class to return
    battleresult = Battleresult()

    # pokemon1 attack dmg
    battleresult.attack1 = attack(pokemon1, pokemon2)
    # pokemon2 attack dmg
    battleresult.attack2 = attack(pokemon2, pokemon1)

    battleresult.pokemon1 = pokemon1
    battleresult.pokemon2 = pokemon2

    if battleresult.attack1 > battleresult.attack2:
        battleresult.winner = pokemon1
        battleresult.loser = pokemon2
    else:
        battleresult.winner = pokemon2
        battleresult.loser = pokemon1

    return (battleresult)


# Calculates the potential damage a pokemon does against another pokemon.
def attack(attacker: Pokemon, defender: Pokemon):

    # A1 / D2 + Type1 * Type2 (Type2 = Type1 if type is not set)
    ad = attacker.Attack / defender.Defense
    pwr = 50 * attacker.getLevelMultiplier()
    dmg = ((pwr + ad) / 50) + 2
    # Compare type 1 and type 2
    type1 = GetComparison(attacker.Type1, defender.Type1)
    # Compare type 2 but make sure type2 is correct.
    type2 = 1
    if attacker.Type2 != 'none' and defender.Type2 != 'none':
        type2 = GetComparison(attacker.Type2, defender.Type2)

    dmg = dmg * type1 * type2
    return (dmg)


# Used to get the type so type2 is comparable.
def getType2(pokemon: Pokemon):
    if pokemon.Type2 == 'none':
        return pokemon.Type1
    else:
        return pokemon.Type1
