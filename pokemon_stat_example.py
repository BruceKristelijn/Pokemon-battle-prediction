from pokemon.pokemon import get_pokemon
from pokemon.pokemon import MAX_STATE_XP

# Get bulbasaur
bulb = get_pokemon(1)
bulb.setLevel(100)

print(bulb.get_attack(15, MAX_STATE_XP)) # should be 196
print(bulb.get_defense(15, MAX_STATE_XP)) # should be 196
print(bulb.get_speed(15, MAX_STATE_XP)) # should be 188
print(bulb.get_special(15, MAX_STATE_XP)) # should be 228