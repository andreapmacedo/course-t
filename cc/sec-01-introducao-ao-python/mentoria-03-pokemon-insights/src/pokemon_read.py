import csv


def read_pokemon_data(path):
    with open(path) as csv_file:
        pokedex = csv.DictReader(csv_file)
        # pokedex_list = []
        # for pokemon in pokedex:
        #     pokedex_list.append(pokemon)
        pokedex_list = list(pokedex)
        return pokedex_list

# def read_pokemon_data(path):
#     with open('pokemon.csv', 'r') as csv_file:
#         reader = csv.reader(csv_file)

print(read_pokemon_data("data/Pokemon.csv")[0])
# print(read_pokemon_data("data/Pokemon.csv"))