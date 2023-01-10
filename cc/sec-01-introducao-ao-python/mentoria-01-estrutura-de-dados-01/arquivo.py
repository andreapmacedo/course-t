# %%
altura = [1.73, 1.68, 1.71, 1.89, 1.79]

altura[0] # 1.73

# %%
print(altura[-1]) # 1.79 (último elemento)
# %%
print(altura[1:3]) # [1.68, 1.71] (segundo e terceiro elementos)

# %%
print(altura[1:]) # [1.68, 1.71, 1.89, 1.79] (segundo até o último elemento)

# %%
print(altura[:3]) # [1.73, 1.68, 1.71] (primeiro até o terceiro elemento)

# %%
print(altura[:]) # [1.73, 1.68, 1.71, 1.89, 1.79] (todos os elementos)

# fatiamento

# %%
print(altura[::2]) # [1.73, 1.71, 1.79] (todos os elementos, pulando de 2 em 2)

# %%
print(altura[:4:2]) # [1.73, 1.71] (primeiro até o quarto elemento, pulando de 2 em 2)

# %%
nome = "Python"
print(nome[::-1]) # nohtyP (inverso)

print(nome[::2]) # Pto (pulando de 2 em 2)

print(nome[1::2]) # yhn (pulando de 2 em 2, começando no segundo elemento)

print(nome[1:4:2]) # yh (pulando de 2 em 2, começando no segundo elemento, até o quarto)

print(sorted(nome)) # ['P', 'h', 'n', 'o', 't', 'y']

print(sorted(nome, reverse=True)) # ['y', 't', 'o', 'n', 'h', 'P']

print(nome)

nome.sort() # AttributeError: 'str' object has no attribute 'sort'
print(nome)



# %%
if 1.73 in altura:
    print("Existe")


# %%
altura.append(1.82)

# %%
lista_ordenada = altura.sort()
print(altura)


# %%
a, *b, c = altura
print(a) # 1.73 (primeiro elemento)
print(b) # [1.68, 1.71, 1.89] (segundo até o penúltimo elemento)
print(c) # 1.82 (último elemento)

# %%
nova_lista = [['andre', 1.77], ['carol', 1.60]]

for item in nova_lista:
    print(item)
    print(item[0], item[1])

# desempacotamento
# %%
for name, height in nova_lista:
    print(name, height) # andre 1.77
# %%

outra_lista = [['andre', 1.77], ['carol', 1.60, 'feminino']]

for name, height in outra_lista:
    print(name, height) # vai dar erro pois o segundo elemento da lista tem 3 elementos

# %%
dicionario = {'andre': 1.77, 'carol': 1.60}
for name, height in dicionario.items():
    print(name, height) # andre 1.77

# %%
for name in dicionario.keys():
    print(name) # andre

# %%    
for height in dicionario.values():
    print(height) # 1.77


# %%
novo_dicionario = dict(nova_lista)
print(novo_dicionario) # {'andre': 1.77, 'carol': 1.6}


# %%
outro_dicionario = dict()
for name, height in nova_lista:
    outro_dicionario[name] = height

print(outro_dicionario) # {'andre': 1.77, 'carol': 1.6}

# dict comprehension
# %%
dicionario2 = { name: height for name, height in nova_lista }
print(dicionario2) # {'andre': 1.77, 'carol': 1.6}

# list comprehension
# %%
height_in_feet = [round(height * 3.28084, 2) for height in altura]
print(height_in_feet) # [5.69, 5.51, 5.59, 6.22, 5.87, 5.98]

# %%
height_in_feet_with_if_1 = [round(height * 3.28084, 2) for height in altura if height > 1.80]
print(height_in_feet_with_if_1) # [6.22]

# %%
height_in_feet_with_if_2 = [round(height * 3.28084, 2) if height > 1.70 else 0 for height in altura ]
print(height_in_feet_with_if_2) # [5.68, 0, 5.61, 6.2, 5.87]

# com identação
# %%
height_in_feet_with_if_3 = [
    round(height * 3.28084, 2)
    if height > 1.70 else 0
    for height in altura 
    ]
print(height_in_feet_with_if_3) # [5.68, 0, 5.61, 6.2, 5.87]