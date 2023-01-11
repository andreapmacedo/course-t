import csv


def read_pokemon_data(path):
    with open(path) as csv_file:
        pokedex = csv.DictReader(csv_file)
        
        # forma 1
        # pokedex_list = []
        # for pokemon in pokedex:
        #     pokedex_list.append(pokemon)
        
        # forma 2
        # pokedex_list = [pokemon for pokemon in pokedex]

        # forma 3
        # pokedex_list = list(pokedex)
        # return pokedex_list

        # forma 4
        return list(pokedex)

# def read_pokemon_data(path):
#     with open('pokemon.csv', 'r') as csv_file:
#         reader = csv.reader(csv_file)

print(read_pokemon_data("data/Pokemon.csv")[0])
# print(read_pokemon_data("data/Pokemon.csv"))