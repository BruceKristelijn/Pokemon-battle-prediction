from pokemon.pokemon import Pokemon
from pokemon.pokemontype import get_type_comparison


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

    #CriticalHit
    crit = 1
    randomNumber = random.uniform(1, 100)

    # Check if the number is less than or equal to 6.25
    if randomNumber <= 6.25:
        critical = 2
    
    # Compare type 1 and type 2
    type1 = get_type_comparison(attacker.Type1, defender.Type1)

    # Compare type 2 but make sure type2 is correct other wise type2 stays 1.
    type2 = 1
    if attacker.Type2 != 'none' and defender.Type2 != 'none':
        type2 = get_type_comparison(attacker.Type2, defender.Type2)

    # Calculate attack / defence
    ad = attacker.get_attack() / defender.get_defense()

    # Left side of formula
    dmg = (((((2 * attacker.Level * crit) / 5) + 2) * power * attacker.get_attack() / defender.get_defense()) / 50) + 2

    # Right side of formula
    dmg *= stab * type1 * type2

    randomNumber = random.uniform(1, 100)
    if randomNumber <= accuracy:
        return(dmg)
    else:
        return(0)


# Used to get the type so type2 is comparable.
def getType2(pokemon: Pokemon):
    if pokemon.Type2 == 'none':
        return pokemon.Type1
    else:
        return pokemon.Type1