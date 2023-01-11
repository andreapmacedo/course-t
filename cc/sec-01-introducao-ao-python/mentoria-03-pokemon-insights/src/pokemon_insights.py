from pokemon_read import read_pokemon_data

def get_unique_pokemon_types(path):
    """Retorna uma lista com os tipos únicos dos pokemons.
    """
    pokedex_list = []
    pokedex = read_pokemon_data(path)
    for pokemon in pokedex:
        pokedex_list.append(pokemon["Type 1"])
    
    return list(set(pokedex_list))

def filter_by_pokemon_type(lista_pokemons, tipo_pokemon):
    """Retorna uma lista de pokemons filtrados por tipo.
    """
    filtered_list = []
    for pokemon in lista_pokemons:
        if pokemon["Type 1"] == tipo_pokemon:
            filtered_list.append(pokemon)
    
    return filtered_list



def get_max_attack(path):
    """Retorna o pokemon com maior ataque.
    """
    pokedex = read_pokemon_data(path)
    # max_attack_pokemon = max([int(pokemon["Attack"]) for pokemon in pokedex])
    max_attack_pokemon = max([int(pokemon["Attack"]) for pokemon in pokedex if (pokemon["Attack"]).isnumeric()])
    

    # max_attack = 0
    # max_attack_pokemon = None
    # for pokemon in pokedex:
    #     if int(pokemon["Attack"]) > max_attack:
    #         max_attack = int(pokemon["Attack"])
    #         max_attack_pokemon = pokemon
    
    return max_attack_pokemon


def matches_attack(pokemon, attack: int):
    """Retorna True se o pokemon tem o ataque informado, False caso contrário.
    """
    return int(pokemon["Attack"]) > attack


def filter_by_attack(lista_pokemons, attack: int):
    """Retorna uma lista de pokemons filtrados por ataque.
    """
    return [pokemon for pokemon in lista_pokemons if matches_attack(pokemon, attack)]

    # filtered_list = []
    # for pokemon in lista_pokemons:
    #     if matches_attack(pokemon, attack):
    #         filtered_list.append(pokemon)
    
    # return filtered_list




print(get_unique_pokemon_types("data/Pokemon.csv"))