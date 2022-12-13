# %%
restaurants = [
    {"name": "Restaurante A", "nota": 4.5},
    {"name": "Restaurante B", "nota": 3.0},
    {"name": "Restaurante C", "nota": 4.2},
    {"name": "Restaurante D", "nota": 2.3},
]
# %%
filtered_restaurants = []
min_rating = 3.0
for restaurant in restaurants:
    if restaurant["nota"] > min_rating:
        filtered_restaurants.append(restaurant)
print(filtered_restaurants)  # imprime a lista de restaurantes, sem o B e D

# %%
for index in range(5):
    print(index)


# estrutura de repetição while
# %%
n = 10
last, next = 0, 1
while last < n:
    print(last)
    last, next = next, last + next



# estrutura de repetição enumerate
# %%
languages = ['Python', 'Java', 'JavaScript']

for index, language in enumerate(['Python', 'Java']):
    print(f'{index} - {language}')
# Saída:
# 0 - Python
# 1 - Java
# %%
