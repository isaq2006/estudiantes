from chat import Chat
from datetime import datetime
import uuid

class Clube:
    def __init__(self,  nome="", descricao="", cordenador=None, membros=[], atividades=[]):
        self.__data_criacao = datetime.now()
        self.__id = uuid.uuid4()
        self.__chat = Chat()
        self.__nome = nome
        self.__descricao = descricao
        self.__cordenador = cordenador
        self.__membros = membros
        self.__atividades = atividades
        
    def set_nome(self, nome):
        self.__nome = nome

    def set_descricao(self, descricao):
        self.__descricao = descricao

    def set_cordenador(self, cordenador):
        self.__cordenador = cordenador      
        
    def set_atividades(self, atividades):
        self.__atividades.append(atividades)  
        
    def set_membros(self, membros):
        self.__membros.append(membros)  
        
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
    
    def get_descri(self):
        return self.__descricao
    
    def get_cordenador(self):
        return self.__cordenador

    def solicitar_entrada(self, membro):
        cordenador = self.__cordenador.get_nome()
        membro = self.__membro
        print(f"O cordenador {cordenador} está verificando a solicitação de {membro}")
        self.__membros.append(membro)
        print(f"{membro} foi adicionado ao clube")

    def sair_clube(self, membro):
        # Lógica para sair do clube
        if self.__membros is not None :
            self.__membros.remove(self.__membro)
        else:
            print("Erro: Nenhum membro encontrado no clube")

    def get_imprimirDados(self):
        print("Nome: ", self.__nome)
        print("Descrição: ", self.__descricao)
        print("Cordenador: ", self.__cordenador.get_nome())
        print("Membros: ", self.__membros)
        print("Atividades: ", self.__atividades)
        print("Data de criação: ", self.__data_criacao)
        