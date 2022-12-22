from pokemon.pokemon import get_pokemon
from pokemon.pokemon import MAX_STATE_XP

# Get bulbasaur
bulb = get_pokemon(1)
bulb.setLevel(100)

print(bulb.get_hp(15, MAX_STATE_XP))  # Should go to 293 value.
