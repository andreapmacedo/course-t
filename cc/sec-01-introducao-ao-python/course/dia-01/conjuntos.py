
# %%
permissions = {"member", "group"}  # elementos separados por vírgula, envolvidos por chaves

# %%
permissions

# %%
permissions.add("root")  # adiciona um novo elemento ao conjunto

# %%
permissions.add("member")  # como o elemento já existe, nenhum novo item é adicionado ao conjunto

# %%
permissions.union({"user"})  # retorna um conjunto resultado da união

# %%
print(permissions)

# %%
permissions.intersection({"user", "member"})  # retorna um conjunto resultante da intersecção dos conjuntos

# %%
permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

# permissions.remove("member")  # remove um elemento do conjunto

# permissions.discard("member")  # remove um elemento do conjunto, se ele existir

# permissions.clear()  # remove todos os elementos do conjunto

# permissions.pop()  # remove um elemento aleatório do conjunto

# permissions.update({"user", "group"})  # atualiza o conjunto com os elementos da lista

# permissions.issubset({"user", "group"})  # verifica se o conjunto é um subconjunto do conjunto passado como parâmetro
# %%
