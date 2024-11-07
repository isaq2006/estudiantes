import uuid
class Chat:
    def __init__(self, mensagens=None):
        self.__id = uuid.uuid4()
        self.__mensagens = mensagens

    def get_mensagens(self):
        # Lógica para obter mensagens
        return self.__mensagens

    def send_mensage(self,mensagem):
        # Lógica para enviar mensagens
        self.__mensagens.append(mensagem)
        
    def exibir_mensagens(self):
        # Lógica para exibir mensagens
        for mensagem in self.__mensagens:
            mensagem.exibir_mensagem()
        
