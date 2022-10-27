from pokemon.pokemon import get_pokemon
from util import get_google_key
from pokemon.battle import battle

google_key = get_google_key()

# Get mewtwo
mewtwo = get_pokemon("Mewtwo")
mewtwo.setLevel(100)
mewtwo.print()
# Get weedle
weedle = get_pokemon("Weedle")
weedle.setLevel(100)
weedle.print()
# Perform battle and show result
battle(mewtwo, weedle).print()
