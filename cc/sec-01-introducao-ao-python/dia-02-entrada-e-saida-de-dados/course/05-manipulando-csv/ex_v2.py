# O leitor define como dialeto padrão excel, o que significa dizer que o delimitador de campos será “,“ e o caractere de citação será aspas duplas ("). Uma forma de modificar estes padrões é definindo-os de forma diferente na criação do leitor. Além disso, o leitor irá usar o decodificador padrão do sistema para decodificar em unicode o arquivo .csv. Para utilizar um decodificador diferente, deve ser passado o argumento encoding com o valor do decodificador esperado. Um leitor de .csv pode ser percorrido utilizando o laço de repetição for e, a cada iteração, retorna uma nova linha já transformada em uma lista Python com seus respectivos valores.

import csv

with open("graduacao_unb.csv", encoding="utf8") as file:
    graduacao_reader = csv.reader(file, delimiter=",", quotechar='"')
    # Usando o conceito de desempacotamento
    header, *data = graduacao_reader

group_by_department = {}
for row in data:
    department = row[15]
    if department not in group_by_department:
        group_by_department[department] = 0
    group_by_department[department] += 1

# Escreve o relatório em .csv
# Abre um arquivo para escrita
with open("department_report.csv", "w", encoding = "utf-8") as file:
    writer = csv.writer(file)

    # Escreve o cabeçalho
    headers = [
        "Departamento",
        "Total de Cursos",
    ]
    writer.writerow(headers)

    # Escreve as linhas de dados
    # Desempacotamento de valores
    for department, grades in group_by_department.items():
        # Agrupa o dado com o turno
        row = [
            department,
            grades,
        ]
        writer.writerow(row)
