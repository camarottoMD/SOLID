class Animal: 
    def comer(self):
        print("O animal esta comendo")

    def andar(self):
        print("O animal esta andando na jaula")

# Posso trocar o "Animal" por "Felino" sem que a execução seja alterada, porém o compartamento sera diferente.
class Felino(Animal):
    def lamber(self):
        print("O felino esta lambendo seu pelo")

    # def comer(self):
    #     print("O felino come sua ração")

animal = Animal()
felino = Felino()

animal.comer()
felino.comer()