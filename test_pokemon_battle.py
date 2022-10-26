from pokemon import get_pokemon
from pokemon import get_pokemon_data
from util import get_google_key
from battle import battle

google_key = get_google_key()

# Get bulbasar
bulb = get_pokemon("Mewtwo")
bulb.setLevel(100)
# Get venusaur
weedle = get_pokemon("Weedle")
weedle.setLevel(100)

# Perform battle and show result
battle(bulb, weedle).print()
