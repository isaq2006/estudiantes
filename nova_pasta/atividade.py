class Atividade:
    def __init__(self, titulo: str, descricao: str, data_criacao: float, data_vencimento: float, tipo_arquivo: str, arquivo):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_criacao = data_criacao
        self.__data_vencimento = data_vencimento
        self.__tipo_arquivo = tipo_arquivo
        self.__arquivo = arquivo

    def concluir(self):
        # Lógica para concluir a atividade
        pass

    def visualizar(self):
        # Lógica para visualizar a atividade
        pass

    # Métodos getters
    def get_titulo(self):
        return self.__titulo

    def get_descricao(self):
        return self.__descricao

    def get_data_criacao(self):
        return self.__data_criacao

    def get_data_vencimento(self):
        return self.__data_vencimento

    def get_tipo_arquivo(self):
        return self.__tipo_arquivo

    def get_arquivo(self):
        return self.__arquivo

    # Métodos setters
    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def set_descricao(self, descricao: str):
        self.__descricao = descricao

    def set_data_criacao(self, data_criacao: float):
        self.__data_criacao = data_criacao

    def set_data_vencimento(self, data_vencimento: float):
        self.__data_vencimento = data_vencimento

    def set_tipo_arquivo(self, tipo_arquivo: str):
        self.__tipo_arquivo = tipo_arquivo

    def set_arquivo(self, arquivo):
        self.__arquivo = arquivo
