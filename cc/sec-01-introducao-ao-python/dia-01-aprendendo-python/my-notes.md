Não é possível alterar elementos de uma tupla
ex:
tupla = (1, 2, 3)
tupla[0] = 4
# TypeError: 'tuple' object does not support item assignment

---

###### Dicionários
###### Dicionários são estruturas de dados que mapeiam chaves para valores.
###### Dicionários são mutáveis.
###### Dicionários são representados por chaves {}.
###### Dicionários são iteráveis.
###### Dicionários são indexáveis.
###### Dicionários são heterogêneos.
###### Dicionários são ordenados a partir da versão 3.7 do Python.
###### Dicionários são desordenados a partir da versão 3.7 do Python.

---

###### Tuplas
###### Tuplas são estruturas de dados que armazenam valores.
###### Tuplas são imutáveis.
###### Tuplas são representadas por parênteses ().
###### Tuplas são iteráveis.
###### Tuplas são indexáveis.
###### Tuplas são heterogêneos.
###### Tuplas são ordenadas a partir da versão 3.7 do Python.
###### Tuplas são desordenadas a partir da versão 3.7 do Python.

---

###### Conjuntos
###### Conjuntos são estruturas de dados que armazenam valores.
###### Conjuntos são mutáveis.
###### Conjuntos são representados por chaves {}.
###### Conjuntos são iteráveis.
###### Conjuntos são indexáveis.
###### Conjuntos são heterogêneos.
###### Conjuntos são ordenados a partir da versão 3.7 do Python.
###### Conjuntos são desordenados a partir da versão 3.7 do Python.

---

# Listas
# Listas são estruturas de dados que armazenam valores.
# Listas são mutáveis.
# Listas são representadas por colchetes [].
# Listas são iteráveis.
# Listas são indexáveis.
# Listas são heterogêneos.
# Listas são ordenadas a partir da versão 3.7 do Python.
# Listas são desordenadas a partir da versão 3.7 do Python.

G-cp

#### o que são tipos heterogêneos?

Em Python, tipos heterogêneos referem-se a estruturas de dados que podem conter valores de tipos diferentes. Por exemplo, uma lista em Python pode conter elementos de tipos diferentes, como números inteiros, strings e booleanos:

```python
lista_heterogenea = [10, "vinte", True]
```

Nesse caso, a lista lista_heterogenea contém um número inteiro, uma string e um valor booleano. Essa lista é considerada heterogênea porque ela contém elementos de tipos diferentes.

Em contraste, uma lista homogênea em Python contém apenas elementos de um único tipo. Por exemplo, uma lista de números inteiros é homogênea:

```python
lista_homogenea = [10, 20, 30]
```

Nesse caso, a lista lista_homogenea contém apenas números inteiros e é considerada homogênea.


---

#### ordenar dados em um lista em python

Em Python, você pode ordenar dados em uma lista usando a função sorted() ou o método sort().

A função sorted() retorna uma nova lista ordenada com os elementos da lista original, enquanto o método sort() ordena a lista original em si.

Aqui está um exemplo de como usar a função sorted() para ordenar uma lista de números inteiros:

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

numeros_ordenados = sorted(numeros)

print(numeros_ordenados)
```

A saída do código acima é:

```python
[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

Aqui está um exemplo de como usar o método sort() para ordenar uma lista de números inteiros:

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

numeros.sort()

print(numeros)
```

A saída do código acima é:

```python
[1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

Observe que, por padrão, as funções sorted() e sort() ordenam a lista em ordem crescente. No entanto, você também pode especificar um argumento reverse=True para ordenar a lista em ordem decrescente. Por exemplo:

```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

numeros_ordenados_reverso = sorted(numeros, reverse=True)

print(numeros_ordenados_reverso)
```

A saída do código acima é:

```python
[9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
```

---

### Qual a diferença entre função e método

Em programação, uma função é um bloco de código que pode ser chamado de maneira isolada para realizar uma tarefa específica, geralmente retornando algum valor. As funções podem ser definidas em qualquer lugar do código e são chamadas por seu nome, passando parâmetros (se houver) entre parênteses. Por exemplo:


```python
def somar(a, b):
    return a + b

resultado = somar(3, 4)
print(resultado) # saída: 7

```

Já um método é uma função que está associada a um objeto específico. Em Python, todos os objetos têm métodos, que são funções específicas para esse objeto. Os métodos são chamados usando a sintaxe objeto.metodo(). Por exemplo, se você tem uma lista lista_numeros, você pode usar o método sort() para ordenar a lista diretamente, sem precisar criar uma nova lista:

```python
lista_numeros = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
lista_numeros.sort()
print(lista_numeros) # saída: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

Observe que, neste caso, você não precisa definir a função sort() em nenhum lugar. Ela já está disponível como um método da lista.

Em resumo, a principal diferença entre função e método é que uma função é um bloco de código isolado que pode ser chamado em qualquer lugar do código, enquanto um método é uma função específica para um objeto, que pode ser chamada usando a sintaxe objeto.metodo().

---

