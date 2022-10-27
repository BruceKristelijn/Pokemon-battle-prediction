import unittest

from pokemon.pokemon import get_pokemon
from pokemon.pokemon import MAX_STATE_XP

# test calculations for hp stat
class TestPokemonStatCalculations(unittest.TestCase):
    # Attack
    def test_calculate_attack_stat_max(self):
        # Get bulbasaur
        bulb = get_pokemon(1)
        bulb.setLevel(100)

        # Should go to 196 value.
        attack = bulb.get_attack(15, MAX_STATE_XP)
        self.assertEqual(attack, 196)
    def test_calculate_attack_stat_min(self):
        # Get bulbasaur
        bulb = get_pokemon(1)
        bulb.setLevel(1)

        # Should go to 5 value.
        attack = bulb.get_attack(0, 0)
        self.assertEqual(attack, 5)

    # Defence
    def test_calculate_defence_stat_max(self):
        # Get bulbasaur
        bulb = get_pokemon(1)
        bulb.setLevel(100)

        # Should go to 196 value.
        defence = bulb.get_defense(15, MAX_STATE_XP)
        self.assertEqual(defence, 196)
    def test_calculate_defence_stat_min(self):
        # Get bulbasaur
        bulb = get_pokemon(1)
        bulb.setLevel(1)

        # Should go to 5 value.
        defence = bulb.get_defense(0, 0)
        self.assertEqual(defence, 5)

    # Speed
    def test_calculate_speed_stat_max(self):
        # Get bulbasaur
        bulb = get_pokemon(1)
        bulb.setLevel(100)

        # Should go to 188 value.
        speed = bulb.get_speed(15, MAX_STATE_XP)
        self.assertEqual(speed, 188)
    def test_calculate_speed_stat_min(self):
        # Get bulbasaur
        bulb = get_pokemon(1)
        bulb.setLevel(1)

        # Should go to 5 value.
        speed = bulb.get_speed(0, 0)
        self.assertEqual(speed, 5)

    # Special
    def test_calculate_special_stat_max(self):
        # Get bulbasaur
        bulb = get_pokemon(1)
        bulb.setLevel(100)

        # Should go to 228 value.
        special = bulb.get_special(15, MAX_STATE_XP)
        self.assertEqual(special, 228)
    def test_calculate_special_stat_min(self):
        # Get bulbasaur
        bulb = get_pokemon(1)
        bulb.setLevel(1)

        # Should go to 6 value.
        special = bulb.get_special(0, 0)
        self.assertEqual(special, 6)
if __name__ == '__main__':
    unittest.main()