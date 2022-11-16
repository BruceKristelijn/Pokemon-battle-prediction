import pandas as pd
import requests
from util import get_google_key


# Define method for creating a table to generate a matrix to get the type comparison.
def get_typetable():
    # define the url to get csv from and use API key from config file.
    url = f"https://www.googleapis.com/drive/v3/files/1JkhsIisiKwZO_xV9tJ_W2K46gJVKYeyTKz-DYonQ8LQ/export?key={get_google_key()}&mimeType=text/csv"

    # Get the file from url and write to filename.
    file_name = 'pokemontypedata.csv'

    try:
        f = open(file_name, "r")
        f.read()
    except:
        url = url
        r = requests.get(url, stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content():
                f.write(chunk)

    # define pandas dataframe/
    df = pd.read_csv(file_name)

    # start matrix dictionary to start from.
    matrix = {}

    return df


# Method for easly getting the comparison of two types.
def get_type_comparison(attacker, defender):
    df = get_typetable()
    row = df.loc[df['attacker'] == attacker][defender]
    try:
        return row.item()
    except:
        return 1