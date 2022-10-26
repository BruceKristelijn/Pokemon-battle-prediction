from os import getenv
from dotenv import load_dotenv

def get_google_key():
    load_dotenv()
    return getenv("GOOGLE_KEY")
