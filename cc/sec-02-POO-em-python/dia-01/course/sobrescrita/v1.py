

class Liquidificador(Eletrodomestico):
    def esta_ligado(self):
        return False


class Liquidificador(Eletrodomestico):
    def esta_ligado(self):
        return "Sim" if super().esta_ligado() else "Não"        