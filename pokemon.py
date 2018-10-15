import requests
import pprint

pokemon_url = "https://pokeapi.co/api/v2/pokemon/"
#pokemon_url = "https://pokeapi.co/api/v2/item/240/"
#pokemon_url = "https://pokeapi.co/api/v2/evolution-chain/5/"

def call_API(url):
    response = requests.request("GET", url)
    response_json = response.json()
    formatted_print = pprint.PrettyPrinter()
    formatted_print.pprint(response_json)

if __name__ == "__main__":
    call_API(pokemon_url)