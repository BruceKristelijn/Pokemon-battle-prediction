from pokemon.pokemon import get_pokemon
from pokemon.pokemontype import GetComparison

bulb = get_pokemon(1)
mew = get_pokemon(4)

bulb.print()
bulb.setLevel(65)
bulb.print()

# print((GetComparison(mew.Type1, bulb.Type1) / 2) * 100)
