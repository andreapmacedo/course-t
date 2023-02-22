# %%
people_by_id = {1: "Maria", 2: "Fernanda", 3: "Felipe"}  # elementos no formato "chave: valor" separados por vírgula, envolvidos por chaves

# %%
people_by_name = {"Maria": 1, "Fernanda": 2, "Felipe": 3}  # outro exemplo, dessa vez usando strings como chaves. As aspas são necessárias para que o Python não ache que `Maria`, `Fernanda` e `Felipe` sejam variáveis.

# elementos são acessados por suas chaves
# %%
people_by_id[1]  # saída: Maria

# elementos podem ser removidos com a palavra chave del
# %%
del people_by_id[1]
people_by_id.items()  # dict_items([(1, "Maria"), (2, "Fernanda"), (3, "Felipe")])
# um conjunto é retornado com tuplas contendo chaves e valores

# %%

#gpt

# could you give me examples of iteration with dictionaries?

# %%
# 1. Iterating over dictionary keys:
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key in my_dict:
    print(key)



# %%
# 2. Iterating over dictionary values:
my_dict = {'a': 1, 'b': 2, 'c': 3}

for value in my_dict.values():
    print(value)


# %%
# 3. Iterating over dictionary items (key-value pairs):
my_dict = {'a': 1, 'b': 2, 'c': 3}

for key, value in my_dict.items():
    print(key, value)


# %%
# 4. You can also use the in keyword to check if a key is present in the dictionary:
my_dict = {'a': 1, 'b': 2, 'c': 3}

if 'b' in my_dict:
    print('Key "b" is present in the dictionary')


## there are other ways to do it?

# Using the enumerate() function to iterate over the dictionary keys and their corresponding indices:
# %%
my_dict = {'a': 1, 'b': 2, 'c': 3}

for i, key in enumerate(my_dict):
    print(i, key)


# Using the items() method to create a list of the dictionary key-value pairs, which can then be sorted:
# %%
my_dict = {'a': 1, 'b': 2, 'c': 3}

sorted_items = sorted(my_dict.items())

for key, value in sorted_items:
    print(key, value)



#Using the zip() function to iterate over multiple dictionaries at once:
# %%
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

for key1, key2 in zip(dict1, dict2):
    print(key1, dict1[key1], key2, dict2[key2])



# %%
