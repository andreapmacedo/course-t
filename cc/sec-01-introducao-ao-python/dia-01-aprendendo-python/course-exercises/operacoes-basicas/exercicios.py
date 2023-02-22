# Exercício 1: No terminal, inicialize duas variáveis a e b, sendo a = 10 e b = 5. Mostre o resultado das 7 operações básicas (soma, subtração, multiplicação, divisão, divisão inteira, potenciação e módulo) envolvendo essas variáveis.
# %%
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a ** b)
print(a % b)

#Exercício 2: Declare e inicialize uma variável: hours = 6. Quantos minutos têm em 6 horas? E quantos segundos? Declare e inicialize variáveis minutes e seconds que recebem os respectivos resultados das contas. Depois, imprima cada uma delas.
# %%
hours = 6
minutes = hours * 60
seconds = minutes * 60
print(minutes)
print(seconds)

#Exercício 3: Teste e verifique o que acontece se você colocar um ponto e vírgula no final de uma instrução em Python.
# %%
a = 10;


#Exercício 4: Suponha que o preço de capa de um livro seja R$ 24,20, mas as livrarias recebem um desconto de 40%. O transporte custa 3,00 para o primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias? Escreva uma expressão que receba o custo total e a imprima.
# %%
price = 24.20
discount = 0.4
transport = 3.00
additional_transport = 0.75
copies = 60
print(price * (1 - discount))
print(transport + (copies - 1) * additional_transport)
print(((price * (1 - discount)) * copies) + transport + (copies - 1) * additional_transport)

#or
# %%

books = 60
book_price = (1 - 0.4) * 24.20
print(book_price)
logistic = 3 + (books - 1) * 0.75
print(logistic)
cost = books * book_price + logistic
print(cost)


# %%
