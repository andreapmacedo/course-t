

###### Conjuntos
###### Conjuntos são estruturas de dados que armazenam valores.
###### Conjuntos são mutáveis.
###### Conjuntos são representados por chaves {}.
###### Conjuntos são iteráveis.
###### Conjuntos são indexáveis.
###### Conjuntos são heterogêneos.
###### Conjuntos são ordenados a partir da versão 3.7 do Python.
###### Conjuntos são desordenados a partir da versão 3.7 do Python.

Sintaxe:

```python
permissions = {"member", "group"}  # elementos separados por vírgula, envolvidos por chaves

permissions.add("root")  # adiciona um novo elemento ao conjunto

permissions.add("member")  # como o elemento já existe, nenhum novo item é adicionado ao conjunto

permissions.union({"user"})  # retorna um conjunto resultado da união

permissions.intersection({"user", "member"})  # retorna um conjunto resultante da intersecção dos conjuntos

permissions.difference({"user"})  # retorna a diferença entre os dois conjuntos

```

