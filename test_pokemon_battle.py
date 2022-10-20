from pokemon import GetPokemon
from battle import battle

# Get bulbasar
bulb = GetPokemon("Mewtwo")
bulb.setLevel(100)
# Get venusaur
venusaur = GetPokemon("Weedle")
venusaur.setLevel(100)

# Perform battle and show result
battle(bulb, venusaur).print()
