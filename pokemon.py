import pandas as pd
import requests
import config

BASELEVEL = 50

# Define method for creating a table to generate a matrix to get the type comparison.


def GetPokemonTable():
    # define the url to get csv from and use API key from config file.
    url = "https://www.googleapis.com/drive/v3/files/1ax91ecQyQbLosX2f_yeSq0UREjMFP0GbNCavXg0kpzw/export?key=" + \
        config.key + "&mimeType=text/csv"

    # Get the file from url and write to filename.
    file_name = 'pokemondata.csv'
    r = requests.get(url, stream=True)
    with open(file_name, 'wb') as f:
        for chunk in r.iter_content():
            f.write(chunk)

    # define pandas dataframe/
    df = pd.read_csv(file_name)

    return df

# Get pokemon based on ID


def GetPokemon(id):
    # Check if id is int
    if (type(id) is int):
        # Check ID to prevent turn over.
        if (id <= 0):
            id = 1
        df = GetPokemonTable()
        return Pokemon(df.iloc[id - 1])

    # Check if id is string
    if (type(id) is str):
        df = GetPokemonTable()
        return Pokemon(df.loc[df['Name'] == id].iloc[0])


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
