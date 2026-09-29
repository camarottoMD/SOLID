#pdf, txt, planilhas

from abc import ABC, abstractmethod

class Document(ABC):

    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass
    
    @abstractmethod
    def format(self): pass
    
    @abstractmethod
    def calculate(self): pass

# class PDF(Document):
#     def load(self):
#         print("Load in pdf")

#     def view(self):
#         print("View informations")

#     # Tenho que adicionar o calculate e format para conseguir instanciar a classe,
#     # pois ela esta como algo generico, e adicionar algo que não irei utilizar, essa 
#     # é a maneira incorreta. Agora então devemos segregar as classes
#     def calculate(self):
#         print("No use")

#     def format(self):
#         print("No use")

class DocumentPDF: #ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

class DocumentTXT: #ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def view(self): pass

class DocumentExcel: #ISP
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def calculate(self): pass

document1 = DocumentPDF()
document2 = DocumentTXT()
document3 = DocumentExcel()