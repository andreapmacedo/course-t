# %%
cities_list = [('Andre', 'Rio de Janeiro'), ('Paulo', 'Belo Horizonte')]


# %%
for nome, cidade in cities_list:
    print(nome, cidade)


# %%
cities_dict = {}

for nome, cidade in cities_list:
    cities_dict[nome] = cidade

# %%
print(cities_dict)

# %%
cities_dict["Guilherme"] = "São Paulo"
print(cities_dict)    

# %%
print(cities_dict["Guilherme"])

# %%
print(cities_dict.get("Guilherme"))

# %%
if "São Paulo" in cities_dict.values():
    print("São Paulo está na lista")

# %%
cities_dict2 = { nome: cidade for nome, cidade in cities_list }
print(cities_dict2)

# %%
cities_dict3 = dict(cities_list)
print(cities_dict3)


# %%
conjunto = set()
conjunto.add("São Paulo")
conjunto.add("Rio de Janeiro")
conjunto.add("Santo Andre")

conjunto_dois = set({"Rio de Janeiro", "Recife"})


# %%
print(conjunto.difference(conjunto_dois))