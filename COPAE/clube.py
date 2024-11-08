# Importa as bibliotecas necessárias
from chat import Chat  # Importa a classe Chat para gerenciar as mensagens do clube
from datetime import datetime  # Importa para registrar a data de criação do clube
import uuid  # Importa para gerar um ID único para o clube

# Definição da classe Clube
class Clube:
    def __init__(self, nome="", descricao="", cordenador=None, membros=[], atividades=[]):
        # Inicializa atributos do clube
        self.__data_criacao = datetime.now()  # Define a data de criação como o momento atual
        self.__id = uuid.uuid4()  # Gera um ID único para o clube
        self.__chat = Chat()  # Cria um objeto Chat para gerenciar as mensagens do clube
        self.__nome = nome  # Nome do clube
        self.__descricao = descricao  # Descrição do clube
        self.__cordenador = cordenador  # Coordenador do clube
        self.__membros = membros  # Lista de membros do clube
        self.__atividades = atividades  # Lista de atividades do clube
        
    # Métodos setters para definir valores
    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_cordenador(self, cordenador):
        self.__cordenador = cordenador      
        
    def set_atividades(self, atividades):
        self.__atividades.append(atividades)  
        
    def set_membros(self, membros):
        if membros is not None and isinstance(membros, list):
            for membro in membros:
                if membro is not None:
                    self.__membros.append(membro)
        elif membros is not None:
            self.__membros.append(membros)  
    
    # Métodos getters para acessar os valores
    def get_atividades(self):
        return self.__atividades
        
    def get_mensagens(self):
        return self.__chat.get_mensagens()

    def get_id(self):
        return self.__id

    def get_data_criacao(self):
        return self.__data_criacao

    def get_chat(self):
        return self.__chat

    def get_membros(self):
        return self.__membros

    def get_nome(self):
        return self.__nome
    
    def get_descricao(self):
        return self.__descricao
    
    def get_cordenador(self):
        return self.__cordenador

    # Método para solicitar a entrada de um novo membro no clube
    def solicitar_entrada(self, membro):
        cordenador = self.__cordenador.get_nome()  # Obtém o nome do coordenador
        print(f"O coordenador {cordenador} está verificando a solicitação de {membro.get_nome()}")
        self.__membros.append(membro)  # Adiciona o membro à lista de membros
        print(f"{membro.get_nome()} foi adicionado ao clube")

    # Método para um membro sair do clube
    def sair_clube(self, membro):
        if membro in self.__membros:  # Verifica se o membro está na lista
            self.__membros.remove(membro)  # Remove o membro da lista
            print(f"{membro.get_nome()} saiu do clube")
        else:
            print("Erro: Membro não encontrado no clube")

    # Método para exibir os dados do clube
    def get_imprimirDados(self):
        print("Nome: ", self.__nome)
        print("Descrição: ", self.__descricao)
        print("Coordenador: ", self.__cordenador.get_nome() if self.__cordenador else "Nenhum")
        print("Membros: ", [membro.get_nome() for membro in self.__membros])
        print("Data de criação: ", self.__data_criacao)
