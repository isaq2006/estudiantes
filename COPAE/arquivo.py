from datetime import datetime

class Arquivo:
    def __init__(self, titulo="", autores="", id_autor="", data_envio="", conteudo=""):
        self.__titulo = titulo
        self.__autores = autores
        self.__id_autor = id_autor
        self.__conteudo = conteudo
        self.__data_envio = datetime.now()

    def enviar_arquivo(self):
        # Lógica para enviar o arquivo
        print("digite o tiutlo do arquivo")
        self.__titulo = input()
        print("digite os autores do arquivo")
        self.__autores = input()
        print("digite o conteudo do arquivo")
        self.__conteudo = input()

    def cancelar_envio(self):
        # Lógica para cancelar o envio do arquivo
        del self

    def editar_arquivo(self, id_autor):
        """Edita o envio do arquivo"""
        self.__id_autor = id_autor
        print("Voce deseja editar qual dado do seu envio?")
        print("[1] Titulo")
        print("[2] Autores")
        print("[3] Conteudo")

        choice = input()

        if choice == "1":
            self.__titulo = input("Digite o novo titulo do arquivo: ")
        elif choice == "2":
            self.__autores = input("Digite os novos autores do arquivo: ")
        elif choice == "3":
            self.__conteudo = input("Digite o novo conteudo do arquivo: ")
            
    def editar_envio(self, id_autor):
        # Lógica para editar o envio do arquivo
        if id_autor != self.set_id_autor:
            print("você não é o autor desta atividade")
        else:
            print("voce deseja editar qual dado do seu envio?\n[1] Titulo\n[2] Autores\n[3] Conteudo")
            decisao = input()
            if decisao == "1":
                print("digite o novo tiutlo do arquivo")
                self.__titulo = input()
            elif decisao == "2":
                print("digite os novos autores do arquivo")
                self.__autores = input()
            elif decisao == "3":
                print("digite o novo conteudo do arquivo")
                self.__conteudo = input()
    def visualizar(self):
        print(f"Titulo: {self.__titulo}")
        print(f"Autores: {self.__autores}")
        print(f"Data de envio: {self.__data_envio}")
        print(f"Conteudo: {self.__conteudo}")
        print("\n")
    # Métodos getters
    def get_titulo(self):
        
        return self.__titulo

    def get_autores(self):
        return self.__autores

    def get_data_envio(self):
        return self.__data_envio
    
    def get_id_autor(self):
        return self.__id_autor

    # Métodos setters
    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def set_autores(self, autores):
        self.__autores = autores
        
    def set_id_autor(self, id):
        self.__id_autor = id

    def set_data_envio(self, data_envio: float):
        self.__data_envio = data_envio
