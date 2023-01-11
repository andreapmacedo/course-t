from src.pokemon_sorting import sort_by


# com return
def test_sort_by():
    pokemons_list = [
        {"Name": "Bulbasaur", "Type 1": "Grass", "Type 2": "Poison", "Total": 318, "HP": 45, "Attack": 49, "Defense": 49, "Sp. Atk": 65, "Sp. Def": 65, "Speed": 45, "Generation": 1, "Legendary": False},
        {"Name": "Ivysaur", "Type 1": "Grass", "Type 2":
            "Poison", "Total": 405, "HP": 60, "Attack": 62, "Defense": 63, "Sp. Atk": 80, "Sp. Def": 80, "Speed": 60, "Generation": 1, "Legendary": False},
        {"Name": "Venusaur", "Type 1": "Grass", "Type 2": "Poison", "Total": 525, "HP": 80, "Attack": 82, "Defense": 83, "Sp. Atk": 100, "Sp. Def": 100, "Speed": 80, "Generation": 1, "Legendary": False},
        {"Name": "Charmander", "Type 1": "Fire", "Type 2": "", "Total": 309, "HP": 39, "Attack": 52, "Defense": 43, "Sp. Atk": 60, "Sp. Def": 50, "Speed": 65, "Generation": 1, "Legendary": False},
        
    ]

    assert sort_by(pokemons_list, "Attack") == [
        {"Name": "Bulbasaur", "Type 1": "Grass", "Type 2": "Poison", "Total": 318, "HP": 45, "Attack": 49, "Defense": 49, "Sp. Atk": 65, "Sp. Def": 65, "Speed": 45, "Generation": 1, "Legendary": False},
        {"Name": "Charmander", "Type 1": "Fire", "Type 2": "", "Total": 309, "HP": 39, "Attack": 52, "Defense": 43, "Sp. Atk": 60, "Sp. Def": 50, "Speed": 65, "Generation": 1, "Legendary": False},
        {"Name": "Ivysaur", "Type 1": "Grass", "Type 2":"Poison", "Total": 405, "HP": 60, "Attack": 62, "Defense": 63, "Sp. Atk": 80, "Sp. Def": 80, "Speed": 60, "Generation": 1, "Legendary": False},
        {"Name": "Venusaur", "Type 1": "Grass", "Type 2": "Poison", "Total": 525, "HP": 80, "Attack": 82, "Defense": 83, "Sp. Atk": 100, "Sp. Def": 100, "Speed": 80, "Generation": 1, "Legendary": False},
    ]
# sem return
# def test_sort_by():
#     pokemons_list = [
#         {"Name": "Bulbasaur", "Type 1": "Grass", "Type 2": "Poison", "Total": 318, "HP": 45, "Attack": 49, "Defense": 49, "Sp. Atk": 65, "Sp. Def": 65, "Speed": 45, "Generation": 1, "Legendary": False},
#         {"Name": "Ivysaur", "Type 1": "Grass", "Type 2":
#             "Poison", "Total": 405, "HP": 60, "Attack": 62, "Defense": 63, "Sp. Atk": 80, "Sp. Def": 80, "Speed": 60, "Generation": 1, "Legendary": False},
#         {"Name": "Venusaur", "Type 1": "Grass", "Type 2": "Poison", "Total": 525, "HP": 80, "Attack": 82, "Defense": 83, "Sp. Atk": 100, "Sp. Def": 100, "Speed": 80, "Generation": 1, "Legendary": False},
#         {"Name": "Charmander", "Type 1": "Fire", "Type 2": "", "Total": 309, "HP": 39, "Attack": 52, "Defense": 43, "Sp. Atk": 60, "Sp. Def": 50, "Speed": 65, "Generation": 1, "Legendary": False},
        
#     ]

#     sort_by(pokemons_list, "Attack")
#     assert sort_by(pokemons_list, "Attack") == [
#         {"Name": "Bulbasaur", "Type 1": "Grass", "Type 2": "Poison", "Total": 318, "HP": 45, "Attack": 49, "Defense": 49, "Sp. Atk": 65, "Sp. Def": 65, "Speed": 45, "Generation": 1, "Legendary": False},
#         {"Name": "Charmander", "Type 1": "Fire", "Type 2": "", "Total": 309, "HP": 39, "Attack": 52, "Defense": 43, "Sp. Atk": 60, "Sp. Def": 50, "Speed": 65, "Generation": 1, "Legendary": False},
#         {"Name": "Ivysaur", "Type 1": "Grass", "Type 2":"Poison", "Total": 405, "HP": 60, "Attack": 62, "Defense": 63, "Sp. Atk": 80, "Sp. Def": 80, "Speed": 60, "Generation": 1, "Legendary": False},
#         {"Name": "Venusaur", "Type 1": "Grass", "Type 2": "Poison", "Total": 525, "HP": 80, "Attack": 82, "Defense": 83, "Sp. Atk": 100, "Sp. Def": 100, "Speed": 80, "Generation": 1, "Legendary": False},
#     ]