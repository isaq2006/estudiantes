# Importa o módulo datetime para gerenciar a data de envio do arquivo
from datetime import datetime

# Definição da classe Arquivo
class Arquivo:
    def __init__(self, titulo="", autores="", id_autor="", data_envio="", conteudo=""):
        # Inicializa os atributos do arquivo com valores padrão ou recebidos no construtor
        self.__titulo = titulo  # Título do arquivo
        self.__autores = autores  # Nomes dos autores do arquivo
        self.__id_autor = id_autor  # ID do autor para controle de edição
        self.__conteudo = conteudo  # Conteúdo do arquivo
        self.__data_envio = datetime.now()  # Define a data de envio como a data atual

    # Método para enviar um arquivo, solicitando ao usuário as informações necessárias
    def enviar_arquivo(self):
        print("Digite o título do arquivo")
        self.__titulo = input()  # Define o título do arquivo
        print("Digite os autores do arquivo")
        self.__autores = input()  # Define os autores do arquivo
        print("Digite o conteúdo do arquivo")
        self.__conteudo = input()  # Define o conteúdo do arquivo

    # Método para cancelar o envio do arquivo, deletando a instância
    def cancelar_envio(self):
        del self  # Exclui o objeto de arquivo


    # Outro método de edição que verifica o ID do autor antes de permitir a edição
    def editar_envio(self, id_autor):
        # Verifica se o usuário é o autor do arquivo antes de permitir a edição
        if id_autor != self.get_id_autor():
            print("Você não é o autor desta atividade")
        else:
            print("Você deseja editar qual dado do seu envio?\n[1] Título\n[2] Autores\n[3] Conteúdo")
            decisao = input()
            # Solicita ao usuário a nova informação com base na opção escolhida
            if decisao == "1":
                print("Digite o novo título do arquivo")
                self.__titulo = input()
            elif decisao == "2":
                print("Digite os novos autores do arquivo")
                self.__autores = input()
            elif decisao == "3":
                print("Digite o novo conteúdo do arquivo")
                self.__conteudo = input()

    # Método para visualizar as informações do arquivo
    def visualizar(self):
        print(f"Título: {self.__titulo}")
        print(f"Autores: {self.__autores}")
        print(f"Data de envio: {self.__data_envio}")
        print(f"Conteúdo: {self.__conteudo}")
        print("\n")

    # Métodos getters para acessar os atributos privados
    def get_titulo(self):
        return self.__titulo  # Retorna o título do arquivo

    def get_autores(self):
        return self.__autores  # Retorna os autores do arquivo

    def get_data_envio(self):
        return self.__data_envio  # Retorna a data de envio do arquivo
    
    def get_id_autor(self):
        return self.__id_autor  # Retorna o ID do autor do arquivo

    # Métodos setters para modificar os atributos privados
    def set_conteudo(self, conteudo):
        self.__conteudo = conteudo  # Define um novo conteúdo para o arquivo
    def set_titulo(self, titulo: str):
        self.__titulo = titulo  # Define um novo título para o arquivo

    def set_autores(self, autores):
        self.__autores = autores  # Define novos autores para o arquivo
        
    def set_id_autor(self, id):
        self.__id_autor = id  # Define um novo ID de autor para o arquivo

    def set_data_envio(self, data_envio: float):
        self.__data_envio = data_envio  # Define uma nova data de envio para o arquivo