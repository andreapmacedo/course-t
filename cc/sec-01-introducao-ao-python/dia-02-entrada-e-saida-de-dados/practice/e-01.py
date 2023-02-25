# Exercício 1:
# Faça um programa que receba um nome e imprima o mesmo na vertical em escada invertida. Exemplo: Entrada:

# %%
name = input("Digite seu nome: ")
for i in range(len(name)):
    print(name[i:]) #  [i:] -> pega do índice i até o final

# ou 

# %%
def vertical_inverted_ladder(word):
    for removed_letters in range(len(word)):
        for index in range(len(word) - removed_letters):
            print(word[index], end="")
        print()

if __name__ == "__main__":
    name = input("Digite um nome: ")
    vertical_inverted_ladder(name)     

#Exercício 2:
#Jogo da palavra embaralhada. Desenvolva um jogo em que a pessoa usuária tenha que adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de palavras e escolherá uma aleatoriamente. O jogador terá três tentativas para adivinhar a palavra. Ao final, a palavra deve ser mostrada na tela, informando se a pessoa ganhou ou perdeu o jogo.

#🦜 Para embaralhar uma palavra faça: scrambled_word = "".join(random.sample(word, len(word)))

#🦜 O sorteio de uma palavra aleatória pode ser feito utilizando o método choice: random.choice(["word1", "word2", "word3"]) -> "word2".

# %%
import random

words = ["python", "java", "kotlin", "javascript"]
word = random.choice(words)
scrambled_word = "".join(random.sample(word, len(word)))
print("H A N G M A N")
print(scrambled_word)
guess = input("Guess the word: ")
if guess == word:
    print("You survived!")
else:
    print("You are hanged!")


#🚀 Exercício 4:
#Dado o seguinte arquivo no formato JSON, leia seu conteúdo e calcule a porcentagem de livros em cada categoria em relação ao número total de livros. O resultado deve ser escrito em um arquivo no formato CSV como o exemplo abaixo.    

# %%
import json
import csv

with open("books.json", "r") as f:
    data = json.load(f) # carrega o arquivo json para a variável data

with open("books.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["category", "percentage"])
    for category, books in data.items():
        writer.writerow([category, len(books) / sum(map(len, data.values())) * 100])





    
# %%
