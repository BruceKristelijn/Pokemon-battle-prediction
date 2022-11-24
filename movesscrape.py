import requests
import csv
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
from pprint import pprint

pokemon_data = pd.read_csv('pokemondata.csv')


def extract_move_table(all_rows, table_type='level'):
    moves = []
    for row in all_rows:
        if 'sorting' in str(row):
            continue

        try:
            cell_nums = row.find_all("td", {"class": "cell-num"})
            first_col = cell_nums[0].text
            power = cell_nums[1].text
            accuracy = cell_nums[2].text

            move_data = {
                table_type: first_col,
                "move": div.find("td", {"class": "cell-name"}).a.find(text=True),
                "type": div.find("td", {"class": "cell-icon"}).a.find(text=True),
                "category": row.find("td", {"class": "cell-icon text-center"}).get("data-filter-value"),
                "power": power,
                "accuracy": accuracy,
            }
            moves.append(move_data)
        except Exception as e:
            print("\nData extraction error:", e)
            breakpoint()

    return moves


pokemon_moves_df = pd.DataFrame(columns=["pokemon_id", "pokemon_name", "level_moveset", "tm_moveset", "hm_moveset"])
for i, pokemon in enumerate(pokemon_data['Name'].str.lower()):
    if pokemon == 'nidoran' and pokemon_data.iloc[i]["Number"] == 29:
        pokemon = f"{pokemon}-f"
        breakpoint()
    URL = f"https://pokemondb.net/pokedex/{pokemon}/moves/1"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    divs = [div for div in soup.find_all("div", {"class": "grid-col span-lg-6"}) if 'Pokémon Red' in str(div)]

    if len(divs) != 2:
        msg = f"Divs variable is not 2. Length: {len(divs)}. Pokemon: {pokemon}"
        print(msg)
        breakpoint()
        raise Exception(msg)

    level_moveset, hm_moveset, tm_moveset = (None, None, None)
    for div in divs:
        if 'Moves learnt by level up' in str(div):
            first_table = div.find_all("table", {"class": "data-table"})[0]
            rows = first_table.find_all("tr")
            level_moveset = extract_move_table(rows)
        else:
            tables = div.find_all("table", {"class": "data-table"})

            # Loops through both table_types HM & TM
            for table in tables:
                table_type = table.th.text
                rows = table.find_all("tr")

                if table_type == 'HM':
                    hm_moveset = extract_move_table(rows, 'hm')

                if table_type == 'TM':
                    tm_moveset = extract_move_table(rows, 'tm')

    if not level_moveset:
        raise Exception(f"No moves found for pokemon: {pokemon}")

    print(f"\nFound moves for pokemon..\n{pokemon} | "
          f"level moves: {len(level_moveset)} | "
          f"hm moves: {len(hm_moveset) if hm_moveset else None} | "
          f"tm moves: {len(tm_moveset) if tm_moveset else None} |\n")

    df = pd.DataFrame([{
                "pokemon_id": pokemon_data.iloc[i]["Number"],
                "pokemon_name": pokemon,
                "level_moveset": level_moveset,
                "hm_moveset": hm_moveset,
                "tm_moveset": tm_moveset
            }])

    pokemon_moves_df = pd.concat([pokemon_moves_df, df], ignore_index=True)


# Save moves to csv
pokemon_moves_df.to_csv('pokemonmovedata.csv', index=False)