class Chat:
    def __init__(self, id: int, mensagens: list):
        self.__id = id
        self.__mensagens = mensagens

    def get_mensage(self):
        # Lógica para obter mensagens
        pass

    def send_mensage(self):
        # Lógica para enviar mensagens
        pass

    # Métodos getters
    def get_id(self):
        return self.__id

    def get_mensagens(self):
        return self.__mensagens

    # Métodos setters
    def set_id(self, id: int):
        self.__id = id

    def set_mensagens(self, mensagens: list):
        self.__mensagens = mensagens
