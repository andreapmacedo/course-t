from personagem import Personagem
from jedi_sith import Jedi, Sith

# personagem1 = Personagem("Frodo", "Hobbit", 120)

# print(personagem1.nome)
# print(personagem1.raca)
# print(personagem1.hp)

# print(vars(personagem1))
personagem1 = Personagem("Padmé", "Humana", 40)
personagem2 = Jedi("Luke", "Humano", 200)
personagem3 = Sith("Vader", "Humano", 300)

print("----------\n")
print("BATALHA")
print(f"{personagem3.nome}: {personagem3.fala()}")
print(f"{personagem2.nome}: {personagem2.fala()}\n\n")

while personagem3.get_hp() > 0:
    print(f"{personagem3.nome} (HP {personagem3.get_hp()}) ataca {personagem2.nome} (HP {personagem2.get_hp()})")
    personagem3.ataque(personagem2)
    personagem2.fala()
    if personagem2.get_hp() > 0:
        print(f"{personagem2.nome} (HP {personagem2.get_hp()}) contra-ataca {personagem3.nome} (HP {personagem3.get_hp()})")
        personagem2.contra_ataque(personagem3)
        personagem3.fala()
    else:
        break
