from typing import Union

import pandas as pd
import requests
from os import getenv
from util import get_google_key


BASELEVEL = 50
valid_pokemon_keys = ['Number', 'Name', 'Types', 'Type1', 'Type2', 'Height', 'Weight',
       'Male_Pct', 'Female_Pct', 'Capt_Rate', 'Exp_Points', 'Exp_Speed',
       'Base_Total', 'HP', 'Attack', 'Defense', 'Special', 'Speed',
       'Evolutions', 'Legendary']


class Pokemon:
    Level = 50

    def __init__(self, data):
        # Set source data.
        self.source = data
        for k, v in data.items():
            setattr(self, k, v)

    def getLevelMultiplier(self):
        return self.Level / BASELEVEL

    def setLevel(self, newlevel):
        if self.Level == newlevel:
            return

        # Set new level and get multiplier.
        self.Level = newlevel
        levelMultiplier = self.getLevelMultiplier()

        # Values to reset.
        # HP Attack Defense Special Speed
        self.HP = self.source.HP * levelMultiplier
        self.Attack = self.source.Attack * levelMultiplier
        self.Defense = self.source.Defense * levelMultiplier
        self.Special = self.source.Special * levelMultiplier
        self.Speed = self.source.Speed * levelMultiplier

    def print(self):
        for k, v in vars(self).items():
            if k != "source":
                print(k + ":", v)

        print("Level multiplier:", self.getLevelMultiplier())
        print("------------")


def get_pokemon_data(auth_key):
    file_name = 'pokemondata.csv'

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

    return pd.read_csv(file_name)


def get_pokemon(id_or_name: Union[int, str]) -> Pokemon:
    df = get_pokemon_data(get_google_key())
    k = id_or_name
    if type(k) is int:
        # Check ID to prevent turn over.
        if k <= 0:
            k = 1
        return Pokemon(df.loc[df['Number'] == k].iloc[0])

    if type(k) is str:
        return Pokemon(df.loc[df['Name'] == k].iloc[0])
