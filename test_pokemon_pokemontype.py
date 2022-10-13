from pokemon import GetPokemon
from pokemontype import GetComparison

bulb = GetPokemon(4)
mew = GetPokemon(1)

print((GetComparison(mew.Type1, bulb.Type1) / 2) * 100)
