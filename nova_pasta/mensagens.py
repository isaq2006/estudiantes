class Mensagem:
    def __init__(self, autor, conteudo: str, data_envio: float, status_leitura: bool):
        self.__autor = autor
        self.__conteudo = conteudo
        self.__data_envio = data_envio
        self.__status_leitura = status_leitura

    def responder_mensagem(self):
        # Lógica para responder a uma mensagem
        pass

    def encaminhar(self):
        # Lógica para encaminhar a mensagem
        pass

    # Métodos getters
    def get_autor(self):
        return self.__autor

    def get_conteudo(self):
        return self.__conteudo

    def get_data_envio(self):
        return self.__data_envio

    def get_status_leitura(self):
        return self.__status_leitura

    # Métodos setters
    def set_autor(self, autor):
        self.__autor = autor

    def set_conteudo(self, conteudo: str):
        self.__conteudo = conteudo

    def set_data_envio(self, data_envio: float):
        self.__data_envio = data_envio

    def set_status_leitura(self, status_leitura: bool):
        self.__status_leitura = status_leitura
