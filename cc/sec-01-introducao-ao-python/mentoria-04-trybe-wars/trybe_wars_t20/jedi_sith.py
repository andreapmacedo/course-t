from personagem import Personagem
from sabre import Sabre
from random import choice


class Jedi(Personagem):
    def __init__(self, nome, raca, hp):
        super().__init__(nome, raca, hp)
        self.sabre_luz = Sabre("verde", 200)

    def defesa(self):
        defesa = choice([True, False])
        if defesa:
            print(f"{self.nome} defendeu")
        return defesa

    def contra_ataque(self, personagem):
        personagem.set_hp(self.sabre_luz.poder)

    def fala(self):
        if self.get_hp() <= 0:
            print(f"{self.nome} morreu")
        return "NOOOOOOOOO!"


class Sith(Personagem):
    def __init__(self, nome, raca, hp):
        super().__init__(nome, raca, hp)
        self.sabre_luz = Sabre("vermelho", 300)

    def ataque(self, personagem):
        if not personagem.defesa():
            personagem.set_hp(self.sabre_luz.poder)

    def fala(self):
        if self.get_hp() <= 0:
            print(f"{self.nome} morreu")
        return "EU SOU SEU PAI!"
