# Tupla é uma estrutura de dados imutável, ou seja, não é possível alterar seus elementos
# %%
user = ("Will", "Marcondes", 42)  # elementos são definidos separados por vírgula, envolvidos por parênteses

# %%
user[0]  # acesso também por índices

# %%
user[2]  # acesso também por índices

# %%
user[0] = "Willian"  # erro: não é possível alterar elementos de uma tupla

# %%
user["Will"]  # erro: não é possível acessar elementos de uma tupla por chaves

