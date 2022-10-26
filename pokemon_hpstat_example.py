from pokemon.pokemon import get_pokemon
from pokemon.pokemon import calculate_hp_stat

# Get bulbasaur
bulb = get_pokemon(1)
bulb.setLevel(100)

hpstat = calculate_hp_stat(bulb.Level, bulb.source.HP, 15, 65535)
print(hpstat) # Should go to 293 value.