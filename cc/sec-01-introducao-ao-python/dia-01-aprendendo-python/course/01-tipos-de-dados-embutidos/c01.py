# Booleanos (bool)
# Os valores booleanos True e False pertencem ao tipo embutido bool.


# Números inteiros (int)
# O primeiro dos tipos numéricos é o int, ele representa um número inteiro, ou seja, é escrito sem parte fracionária.


# Números fracionários (float)
# O segundo tipo numérico é o float, também conhecido por ponto flutuante, ele representa um número decimal ou fracionário.

# Strings (str)
# Além dos tipos numéricos, temos o tipo de sequência de texto str. Ele representa uma cadeia de caracteres ou, como popularmente conhecida, uma string. As strings são definidas envolvendo um valor com aspas simples ou duplas. Exemplo: a = "Olá"

# Temos ainda estruturas do tipo:

# sequência(list, tuple, range);
# conjuntos(set, frozenset);
# mapeamento(dict);
# sequências binárias(bytes, bytearray, memoryview).
# Além dessas temos várias outras, que você pode encontrar acessando os links abaixo:

# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/library/datatypes.html

## Listas (list)

fruits = ["laranja", "maçã", "uva", "abacaxi"]  # elementos são definidos separados por vírgula, envolvidos por colchetes

fruits[0]  # o acesso é feito por índices iniciados em 0

fruits[-1]  # o acesso também pode ser negativo

fruits.append("banana")  # adicionando uma nova fruta

fruits.remove("abacaxi")  # removendo uma fruta

fruits.extend(["pera", "melão", "kiwi"])  # acrescenta uma lista de frutas a lista original

fruits.index("maçã")  # retorna o índice onde a fruta está localizada, neste caso, 1

fruits.sort()  # ordena a lista de frutas

