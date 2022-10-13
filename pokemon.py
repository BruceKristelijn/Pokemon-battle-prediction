import pandas as pd
import requests
import config

# Define method for creating a table to generate a matrix to get the type comparison.
def GetPokemonTable():
    # define the url to get csv from and use API key from config file.
    url = "https://www.googleapis.com/drive/v3/files/1ax91ecQyQbLosX2f_yeSq0UREjMFP0GbNCavXg0kpzw/export?key=" + config.key + "&mimeType=text/csv"

    #Get the file from url and write to filename.
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
    if(type(id) is int):
        # Check ID to prevent turn over.
        if(id <= 0):
            id = 1
        df = GetPokemonTable()
        return df.iloc[id - 1]

    # Check if id is string
    if(type(id) is str):
        df = GetPokemonTable()
        return df.loc[df['Name'] == id].iloc[0]