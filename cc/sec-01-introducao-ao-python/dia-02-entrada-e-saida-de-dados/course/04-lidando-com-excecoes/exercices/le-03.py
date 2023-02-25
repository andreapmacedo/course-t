# Dado um arquivo contendo estudantes e suas respectivas notas, escreva um programa que:

# lê todas essas informações;
# aplique um filtro, mantendo somente as pessoas que estão reprovadas;
# escreva seus nomes em outro arquivo.
# Considere que a nota miníma para aprovação é 6.

recuStudents = []

try:
    arquivo = open("arquivo.txt", "r")
except OSError:
    # será executado caso haja uma exceção
    print("arquivo inexistente")
else:
    # será executado se tudo ocorrer bem no try
    print("arquivo manipulado e fechado com sucesso")
    # print(arquivo, arquivo.read())
    for linha in arquivo:
        print("linha -> ", linha)
        cada_linha = linha.split(" ")
        print("cada linha -> ",cada_linha)
        nome = cada_linha[0]
        nota = cada_linha[1]
        print("nome -> ", nome)
        print("nota -> ", nota)
        if int(nota) < 6:
            
            recuStudents.append(nome+" "+nota)
            # recuStudents.append(nome + "\n")
        # if int(nota) < 6:
        #     print("reprovado")
        #     arquivo2 = open("recuStudentsFile.txt", "a") # a = append (adiciona no final do arquivo) 
        #     arquivo2.write(nome + " " + nota)

    arquivo.close()
    with open("recuStudents.txt", mode="w") as recuStudentsFile:
        print(recuStudents)
        recuStudentsFile.writelines(recuStudents)

    
finally:
    # será sempre executado, independentemente de erro
    print("Tentativa de abrir arquivo")