

###### Dicionários
###### Dicionários são estruturas de dados que mapeiam chaves para valores.
###### Dicionários são mutáveis.
###### Dicionários são representados por chaves {}.
###### Dicionários são iteráveis.
###### Dicionários são indexáveis.
###### Dicionários são heterogêneos.
###### Dicionários são ordenados a partir da versão 3.7 do Python.
###### Dicionários são desordenados a partir da versão 3.7 do Python.

Sintaxe:

```python
people_by_id = {1: "Maria", 2: "Fernanda", 3: "Felipe"}  # elementos no formato "chave: valor" separados por vírgula, envolvidos por chaves

people_by_name = {"Maria": 1, "Fernanda": 2, "Felipe": 3}  # outro exemplo, dessa vez usando strings como chaves. As aspas são necessárias para que o Python não ache que `Maria`, `Fernanda` e `Felipe` sejam variáveis.

# elementos são acessados por suas chaves
people_by_id[1]  # saída: Maria

# elementos podem ser removidos com a palavra chave del
del people_by_id[1]
people_by_id.items()  # dict_items([(1, "Maria"), (2, "Fernanda"), (3, "Felipe")])
# um conjunto é retornado com tuplas contendo chaves e valores

```

