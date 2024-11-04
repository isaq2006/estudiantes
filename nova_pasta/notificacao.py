class Notificacao:
    def __init__(self, conteudo: str, data_envio: float, horario_envio):
        self.__conteudo = conteudo
        self.__data_envio = data_envio
        self.__horario_envio = horario_envio

    def visualizar(self):
        # Lógica para marcar a notificação como visualizada
        pass

    # Métodos getters
    def get_conteudo(self):
        return self.__conteudo

    def get_data_envio(self):
        return self.__data_envio

    def get_horario_envio(self):
        return self.__horario_envio

    # Métodos setters
    def set_conteudo(self, conteudo: str):
        self.__conteudo = conteudo

    def set_data_envio(self, data_envio: float):
        self.__data_envio = data_envio

    def set_horario_envio(self, horario_envio):
        self.__horario_envio = horario_envio
