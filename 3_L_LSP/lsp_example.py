class Animal: 
    def comer(self):
        print("O animal esta comendo")

    def andar(self):
        print("O animal esta andando na jaula")

# Posso trocar o "Animal" por "Felino" sem que a execução seja alterada, porém o compartamento sera diferente.
class Felino(Animal):
    def lamber(self):
        print("O felino esta lambendo seu pelo")

    #isso classifica uma quebra do principio de liskov
    # def comer(self):
    #     print("O felino come sua ração")

class Leao(Felino):
    def rugir(self):
        print("O leão esta rugindo alto ruuaaaar!!!")

class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()

carlos_alberto = Pessoa()
animal = Animal()
felino = Felino()

animal.comer()
felino.comer()
carlos_alberto.observa(animal=felino)