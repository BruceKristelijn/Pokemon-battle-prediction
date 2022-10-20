from pokemon import get_pokemon_data
from os import getenv

from util import get_google_key


if __name__ == "__main__":
    if google_key := get_google_key():
        df = get_pokemon_data(google_key)
        breakpoint()
    else:
        print("No google key found. Please set key in .env and run: source .env")
