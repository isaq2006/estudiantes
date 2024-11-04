class Arquivo:
    def __init__(self, titulo: str, autores, data_envio: float):
        self.__titulo = titulo
        self.__autores = autores
        self.__data_envio = data_envio

    def enviar_arquivo(self):
        # Lógica para enviar o arquivo
        pass

    def cancelar_envio(self):
        # Lógica para cancelar o envio do arquivo
        pass

    def editar_envio(self):
        # Lógica para editar o envio do arquivo
        pass

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
