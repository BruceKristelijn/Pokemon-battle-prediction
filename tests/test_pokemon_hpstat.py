import unittest

from pokemon.pokemon import get_pokemon
from pokemon.pokemon import calculate_hp_stat

# test calculations for hp stat
class TestPokemonStatCalculations(unittest.TestCase):
    def test_calculate_hp_stat_max(self):
        # Get bulbasaur
        bulb = get_pokemon(1)
        bulb.setLevel(100)

        # Should go to 293 value.
        hpstat = calculate_hp_stat(bulb.Level, bulb.source.HP, 15, 65535)
        self.assertEqual(hpstat, 293)

    def test_calculate_hp_stat_min(self):
        # Get bulbasaur
        bulb = get_pokemon(1)
        bulb.setLevel(1)

        # Should go to 293 value.
        hpstat = calculate_hp_stat(bulb.Level, bulb.source.HP, 0, 0)
        self.assertEqual(hpstat, 11)


if __name__ == "__main__":
    unittest.main()
