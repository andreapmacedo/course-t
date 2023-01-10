# %%
class Pet():
    def __init__(self, nome, especie, idade, humano):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.humano = humano



    def __str__(self):
        return f"""
        - Especie {self.especie}
        - Nome {self.nome}
        - Idade {self.idade}
        - Dono {self.humano}
        """


thor = Pet('Thor', 'Cachorro', 5, 'Rafael')
print(thor)


# %%
