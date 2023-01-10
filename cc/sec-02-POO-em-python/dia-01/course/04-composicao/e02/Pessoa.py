
# %%

from Liquidificador import Liquidificador


class Pessoa:
    def __init__(self, nome, saldo_na_conta):
        self.nome = nome
        self.saldo_na_conta = saldo_na_conta
        self.liquidificador = None

    def __str__(self):
        return f"{self.nome} - possui {self.saldo_na_conta} reais em sua conta."


    def comprar_liquidificador(self, liquidificador):
        if liquidificador.preco <= self.saldo_na_conta:
            self.saldo_na_conta -= liquidificador.preco
            self.liquidificador = liquidificador
            print(f"Parabéns, você comprou um liquidificador de {liquidificador.preco} reais.")
        else:
            print(f"Você não tem dinheiro suficiente para comprar um liquidificador de {liquidificador.preco} reais.")

        print(f"Seu atual saldo em conta é {self.saldo_na_conta} reais.")



cozinheiro1 = Pessoa("Jacquin", 1000)
print(cozinheiro1)
cozinheiro2 = Pessoa("Rafael", 1000)

liquidificador_vermelho = Liquidificador(100)
liquidificador_preto = Liquidificador(200)

cozinheiro1.comprar_liquidificador(liquidificador_vermelho)
cozinheiro2.comprar_liquidificador(liquidificador_vermelho)
cozinheiro1.comprar_liquidificador(liquidificador_preto)