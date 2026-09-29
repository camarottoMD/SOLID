# class Company:
#     def do_work(self, worker: int) -> None:
#         if worker == 1:
#             print("Programmer creating code")
#         elif worker == 2:
#             print("Seller selling the product")
#         elif worker == 3:
#             print("Human Resources hiring new devs")
#         # add new worker
#         elif worker == 4:
#             print("Frontend raising bugs for production")
#         else:
#             print("Error, no Worker")

# company = Company()
# company.do_work(4)

#           Aplicando OCP

class Programer:
    def make(self):
        print("Programmer creating code")

class Seller:
    def make(self):
        print("Seller selling the product")

class RH:
    def make(self):
        print("Human Resources hiring new devs")

class Company:
    def do_work(self, worker: any) -> None:
        worker.make()

company = Company()
programmer = Programer()
seller = Seller()
rh = RH()
company.do_work(programmer)
company.do_work(seller)
company.do_work(rh)

# Esta ganhando caracteristicas mas não esta sendo alterado.