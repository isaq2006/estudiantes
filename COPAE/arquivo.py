from datetime import datetime

class Arquivo:
    def __init__(self, titulo="", autores="", data_envio="", conteudo=""):
        self.__titulo = titulo
        self.__autores = autores
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
        self.__conteudo = ""
        self.__autores = ""
        self.__titulo = ""

    def editar_envio(self):
        # Lógica para editar o envio do arquivo
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

    # Métodos getters
    def get_titulo(self):
        return self.__titulo

    def get_autores(self):
        return self.__autores

    def get_data_envio(self):
        return self.__data_envio

    # Métodos setters
    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def set_autores(self, autores):
        self.__autores = autores

    def set_data_envio(self, data_envio: float):
        self.__data_envio = data_envio
