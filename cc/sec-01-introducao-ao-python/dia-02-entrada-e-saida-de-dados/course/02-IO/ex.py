
# 1. - Faça um programa que solicite o nome de uma pessoa usuária e imprima-o na vertical.

# %%
nome = input("Digite seu nome: ")
for letra in nome:
    print(letra)



# 2. Escreva um programa que receba vários números naturais e calcule a soma desses valores. Caso algum valor da entrada seja inválido (por exemplo uma letra), uma mensagem deve ser exibida na saída de erros no seguinte formato: “Erro ao somar valores, {valor} é um valor inválido”. Ao final, você deve imprimir a soma dos valores válidos.
# 🦜 Receba os valores em um mesmo input, solicitando à pessoa usuária que separe-os com um espaço. Receba os valores no formato str e utilize o método split para pegar cada valor separado. O método isdigit, embutido no tipo str, pode ser utilizado para verificar se a string corresponde a um número natural.
# %%
nums = input("Digite os números separados por espaço: ").split()
sum = 0
for num in nums:
    if num.isdigit():
        sum += int(num)
    else:
        print(f"Erro ao somar valores, {num} é um valor inválido", file=sys.stderr)
print(f"A soma dos valores válidos é: {sum}")

# %% 
# outra solução.
nums = input("Insira valores aqui, separados por espaço: ")

numsArr = nums.split(" ")

sum = 0
for num in numsArr:
    if not num.isdigit():
        print(f"Erro ao somar valores, {num} não é um dígito.")
    else:
        sum += int(num)

print(f"A soma dos valores válidos é: {sum}")


# 3. Escreva um programa que receba uma string e imprima a quantidade de caracteres que a string possui.
# %%
entrada = input("Digite uma string: ")
print(len(entrada))




