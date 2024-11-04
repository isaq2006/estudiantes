class Clube:
    def __init__(self, id: str, nome: str, descricao: str, data_criacao: float, cordenador, membros: list, atividades: list, chat):
        self.__id = id
        self.__nome = nome
        self.__descricao = descricao
        self.__data_criacao = data_criacao
        self.__cordenador = cordenador
        self.__membros = membros
        self.__atividades = atividades
        self.__chat = chat

    def solicitar_entrada(self):
        # Lógica para solicitar entrada no clube
        pass

    def sair_clube(self):
        # Lógica para sair do clube
        pass

    # Métodos getters
    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_descricao(self):
        return self.__descricao

    def get_data_criacao(self):
        return self.__data_criacao

    def get_cordenador(self):
        return self.__cordenador

    def get_membros(self):
        return self.__membros

    def get_atividades(self):
        return self.__atividades

    def get_chat(self):
        return self.__chat

    # Métodos setters
    def set_id(self, id: str):
        self.__id = id

    def set_nome(self, nome: str):
        self.__nome = nome

    def set_descricao(self, descricao: str):
        self.__descricao = descricao

    def set_data_criacao(self, data_criacao: float):
        self.__data_criacao = data_criacao

    def set_cordenador(self, cordenador):
        self.__cordenador = cordenador

    def set_membros(self, membros: list):
        self.__membros = membros

    def set_atividades(self, atividades: list):
        self.__atividades = atividades

    def set_chat(self, chat):
        self.__chat = chat
