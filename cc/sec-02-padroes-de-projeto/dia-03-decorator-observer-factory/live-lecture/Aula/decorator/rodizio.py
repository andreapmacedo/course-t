import random
from abc import ABC, abstractmethod

class SellerTeam:
    def __init__(self):  
        self.people = [
            "Cristina",
            "Marcela",
            "Rodrigo",
            "Joao Vitor",
            "Marco",
            "Matheus",
            "Esdras",
            "Lucas",
        ]

class Rotation:     
    def __init__(self, sellerTeam):
        self.sellerTeam = sellerTeam

    def next_seller(self):
        seller = self.sellerTeam.people[0]						# selecionar de forma aleatória
        seller = random.choice(self.sellerTeam.people)
        print(f"A pessoa vendedora selecionado é {seller}")
        return seller

# class Decorator(ABC):
#     def __init__(self, rotation):
#         self.rotation = rotation

#     @abstractmethod
#     def next_seller(self):
#         pass

# class RotationwithInterns(Decorator):
#     def next_seller(self):
#         interns = ["Maria Carolina","Cristiano"]

#         self.rotation.sellerTeam.people += interns
#         self.rotation.next_seller()

if __name__ == "__main__":
    seller_team = SellerTeam()
    list_sellers = seller_team.people
    print(list_sellers)

    rotation = Rotation(seller_team)
    rotation.next_seller()

    # rotation = RotationwithInterns(Rotation(seller_team))
    # rotation.next_seller()