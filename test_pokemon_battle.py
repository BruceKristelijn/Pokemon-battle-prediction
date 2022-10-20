from pokemon import get_pokemon
from battle import battle

# Get bulbasar
bulb = get_pokemon("Mewtwo")
bulb.setLevel(100)
# Get venusaur
venusaur = get_pokemon("Weedle")
venusaur.setLevel(100)

# Perform battle and show result
battle(bulb, venusaur).print()
