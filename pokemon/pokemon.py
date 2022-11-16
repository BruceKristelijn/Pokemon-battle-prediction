from math import sqrt
import math
from tokenize import Number
from typing import Union
from typing import List

import pandas as pd
import requests
from os import getenv
from util import get_google_key

BASELEVEL = 50
MAX_STATE_XP = 65535
DATAFRAME = None

valid_pokemon_keys = ['Number', 'Name', 'Types', 'Type1', 'Type2', 'Height', 'Weight',
       'Male_Pct', 'Female_Pct', 'Capt_Rate', 'Exp_Points', 'Exp_Speed',
       'Base_Total',
       'Evolutions', 'Legendary']

class Pokemon:
    Level = 50

    def __init__(self, data):
        # Set source data.
        self.source = data
        for k, v in data.items():
            if k in valid_pokemon_keys:
                setattr(self, k, v)

    def setLevel(self, newlevel):
        if self.Level == newlevel:
            return

        # Set new level and get multiplier.
        self.Level = newlevel

    def print(self):
        for k, v in vars(self).items():
            if k != "source":
                print(k + ":", v)

        print("HP:", self.get_hp())
        print("Attack:", self.get_attack())
        print("Defence:", self.get_defense())
        print("Special:", self.get_special())
        print("Speed:", self.get_speed())
        print("------------")

    def __eq__(self,other):
        if not isinstance(other, Pokemon):
            # don't attempt to compare against unrelated types
            return False
        return self.Number == other.Number

    def get_hp(self, dv: int = 8, stateXp: int = MAX_STATE_XP) -> int:
        return calculate_hp_stat(self.Level, self.source.HP, dv, stateXp)

    def get_stat(self, basestat: Union[int, str], dv: int = 8, stateXp: int = MAX_STATE_XP) -> int:
        if type(basestat) is str:
            basestat = getattr(self.source, basestat)
        return calculate_stat(self.Level, basestat, dv, stateXp)

    def get_attack(self, dv: int = 8, stateXp: int = MAX_STATE_XP) -> int:
        return self.get_stat("Attack", dv, stateXp)

    def get_defense(self, dv: int = 8, stateXp: int = MAX_STATE_XP) -> int:
        return self.get_stat("Defense", dv, stateXp)

    def get_special(self, dv: int = 8, stateXp: int = MAX_STATE_XP) -> int:
        return self.get_stat("Special", dv, stateXp)

    def get_speed(self, dv: int = 8, stateXp: int = MAX_STATE_XP) -> int:
        return self.get_stat("Speed", dv, stateXp)

def get_pokemon_data(auth_key):
    file_name = 'pokemondata.csv'

    global DATAFRAME
    if(DATAFRAME is None):
        # Try to see if local csv exists, if not download and store it.
        try:
            f = open(file_name, "r")
            f.read()
        except:
            url = f"https://www.googleapis.com/drive/v3/files/1ax91ecQyQbLosX2f_yeSq0UREjMFP0GbNCavXg0kpzw/export?key={auth_key}&mimeType=text/csv"
            r = requests.get(url, stream=True)
            with open(file_name, 'wb') as f:
                for chunk in r.iter_content():
                    f.write(chunk)

        # define pandas dataframe/
        DATAFRAME = pd.read_csv(file_name)


    return DATAFRAME

def get_pokemon(id_or_name: Union[int, str] = "list") -> Pokemon:
    df = get_pokemon_data(get_google_key())
    k = id_or_name

    if(k == "list"):
        list = []
        df = get_pokemon_data(get_google_key())

        for index, row in df.iterrows():
            list.append(Pokemon(row))

        return list

    if type(k) is int:
        # Check ID to prevent turn over.
        if k <= 0:
            k = 1
        return Pokemon(df.loc[df['Number'] == k].iloc[0])

    if type(k) is str:
        return Pokemon(df.loc[df['Name'] == k].iloc[0])

# Calculates the HP stat for a pokemon
def calculate_hp_stat(level: int = BASELEVEL, basestat: int = 45, dv: int = 8, stateXp: int = (MAX_STATE_XP/2)) -> int:
    return math.floor(((((basestat + dv) * 2 + (sqrt(stateXp) / 4)) * level) / 100) + level + 10)

# Calculates the Stat for a pokemon
def calculate_stat(level: int = BASELEVEL, basestat: int = 45, dv: int = 8, stateXp: int = (MAX_STATE_XP/2)) -> int:
    return math.floor(((((basestat + dv) * 2 + (sqrt(stateXp) / 4)) * level) / 100) + 5)