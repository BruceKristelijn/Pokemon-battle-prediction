from pokemon import GetPokemon
from pokemontype import GetComparison

bulb = GetPokemon(1)
mew = GetPokemon(4)

bulb.print()
bulb.setLevel(65)
bulb.print()

# print((GetComparison(mew.Type1, bulb.Type1) / 2) * 100)
