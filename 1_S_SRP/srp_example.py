# class Process:
#     def handle(self, username: str, password, str) -> None:
#         if isinstance(username, str) and isinstance(password, str): # 1
#             print('Acessando o banco de dados...') # 2
#             print('Verificando a existencia do usuario...')
#             print('Cadastro de usuarios realizado com sucesso!') # 3
#         else:
#             self.__raise_error('Dados Invalidos')





#               Aplicando Principio de SRP

class Process:
    def handle(self, username: str, password, str) -> None:
        if self.__verify_input_data(username=username, password=password): # 1
            self.__verify_input_in_database(username=username)
            self.__insert_new_user(username=username, password=password)
        else:
            raise Exception('Dados Invalidos')



    # Separando a validação
    def __verify_input_data(self, username: str, password: str) -> bool:
        return isinstance(username, str) and isinstance(password, str) # true ou false

    # Separando a validação de user no banco
    def __verify_input_in_database(self, username: str) -> None:
        print('Acessando o banco de dados...')
        print('Verificando a existencia do usuario...')

    def __insert_new_user(self, username: str, password: str) -> None:
        print('Cadastro de usuarios realizado com sucesso!')

    def __raise_error(self, message: str) -> Exception:
        raise Exception(message)