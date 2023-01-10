from personagem_interface import PersonagemInterface


class Personagem(PersonagemInterface):
    def __init__(self, nome, raca, hp):
        self.nome = nome
        self.raca = raca
        self.__hp = hp

    def get_hp(self):
        return self.__hp

    # @property
    # def hp(self):
    #     return self.__hp

    def set_hp(self, dano):
        self.__hp -= dano

    def fala(self):
        return "Que a força esteja com você!"
