import math

# trybe
def max_attack_key(pokemon):
    """Retorna o ataque do pokemon.
    """
    try:
        return int(pokemon["Attack"])
    except (KeyError, TypeError,  ValueError):
        return -math.inf

# def sort_by(pokemon_list):
#     """Retorna uma lista de pokemons ordenada.
#     """
#     pokemon_list.sort(key=max_attack_key)
    # return pokemon_list.sort(key=max_attack_key)


# IA
# def max_attack_key(pokemon):
#     """Retorna o ataque do pokemon.
#     """
#     return int(pokemon["Attack"])

# com retunr
def sort_by(pokemon_list, key):
    """Retorna uma lista de pokemons ordenada pela chave informada.
    """
    return sorted(pokemon_list, key=lambda x: x[key])

# sem return
# def sort_by(pokemon_list, key):
#     """Retorna uma lista de pokemons ordenada pela chave informada.
#     """
#     sorted(pokemon_list, key=lambda x: x[key])


def sort_by_id(lista_pokemons):
    """Retorna uma lista de pokemons ordenada pelo id.
    """
    return sorted(lista_pokemons, key=lambda x: int(x["#"]))


def sort_by_name(lista_pokemons):
    """Retorna uma lista de pokemons ordenada pelo nome.
    """
    return sorted(lista_pokemons, key=lambda x: x["Name"])


def max_hp(lista_pokemons):
    """Retorna o pokemon com maior HP.
    """
    return max(lista_pokemons, key=lambda x: int(x["HP"]))


def max_attack(lista_pokemons):
    """Retorna o pokemon com maior ataque.
    """
    return max(lista_pokemons, key=lambda x: int(x["Attack"]))

def get_distance(pokemon_1, pokemon_2):
    """Retorna a distância entre dois pokemons.
    """
    return math.sqrt((int(pokemon_1["HP"]) - int(pokemon_2["HP"]))**2 + (int(pokemon_1["Attack"]) - int(pokemon_2["Attack"]))**2)

def sort_by_distance(lista_pokemons, pokemon):
    """Retorna uma lista de pokemons ordenada pela distância.
    """
    return sorted(lista_pokemons, key=lambda x: get_distance(x, pokemon))

def get_closest_pokemon(lista_pokemons, pokemon):
    """Retorna o pokemon mais próximo.
    """
    return sort_by_distance(lista_pokemons, pokemon)[0]

def get_farthest_pokemon(lista_pokemons, pokemon):
    """Retorna o pokemon mais distante.
    """
    return sort_by_distance(lista_pokemons, pokemon)[-1]

def get_pokemon_by_name(lista_pokemons, name):
    """Retorna o pokemon com o nome informado.
    """
    return [pokemon for pokemon in lista_pokemons if pokemon["Name"] == name][0]


def get_pokemon_by_id(lista_pokemons, id):
    """Retorna o pokemon com o id informado.
    """
    return [pokemon for pokemon in lista_pokemons if pokemon["#"] == id][0]

def get_pokemon_by_type(lista_pokemons, type):
    """Retorna o pokemon com o tipo informado.
    """
    return [pokemon for pokemon in lista_pokemons if pokemon["Type 1"] == type]

def get_pokemon_by_generation(lista_pokemons, generation):
    """Retorna o pokemon com a geração informada.
    """
    return [pokemon for pokemon in lista_pokemons if pokemon["Generation"] == generation]

def get_pokemon_by_legendary(lista_pokemons, legendary):
    """Retorna o pokemon com a legendariedade informada.
    """
    return [pokemon for pokemon in lista_pokemons if pokemon["Legendary"] == legendary]




