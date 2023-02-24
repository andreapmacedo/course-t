# Lista
# %%
fruits = ["laranja", "maçã", "uva", "abacaxi"]

# %%
fruits

# %%
fruits[0]  # o acesso é feito por índices iniciados em 0

# %%
fruits[-1]  # o acesso também pode ser negativo

# %%
fruits.append("banana")  # adicionando uma nova fruta

# %%
fruits.remove("abacaxi")  # removendo uma fruta

# %%
fruits.extend(["pera", "melão", "kiwi"])  # acrescenta uma lista de frutas a lista original

# %%
fruits.index("maçã")  # retorna o índice onde a fruta está localizada, neste caso, 1

# %%
fruits.sort()  # ordena a lista de frutas


# %%

# gt

# could you give me examples of iteration with lists?

# %%
# 1. Iterating over a list:
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)

# %%
# 2. Iterating using a while loop:  
my_list = [1, 2, 3, 4, 5]
i = 0

while i < len(my_list):
    print(my_list[i])
    i += 1

# %%
# 3. Using a list comprehension:
my_list = [1, 2, 3, 4, 5]

new_list = [item * 2 for item in my_list]

print(new_list)

# 4. Using the enumerate function to access both the index and the value of each item in the list:
# %%
my_list = [1, 2, 3, 4, 5]

for i, item in enumerate(my_list):
    print(f"Index {i}: {item}")

# %%

# more examples using list comprehension

# Creating a new list of even numbers from an existing list:
# %%
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_list = [num for num in my_list if num % 2 == 0]

print(even_list)


# Creating a new list of squared numbers from an existing list:
# %%
my_list = [1, 2, 3, 4, 5]

squared_list = [num**2 for num in my_list]

print(squared_list)


# Creating a new list of strings from an existing list of integers:
# %%
my_list = [1, 2, 3, 4, 5]

str_list = [str(num) for num in my_list]

print(str_list)


# Creating a new list of tuples from two existing lists:
# %%
list_a = [1, 2, 3]
list_b = [4, 5, 6]

tuple_list = [(a, b) for a in list_a for b in list_b]

print(tuple_list)



# %%
