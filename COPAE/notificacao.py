from datetime import datetime
class Notificacao:
    def __init__(self, mensagem=None):
        self.__conteudo = mensagem.get_conteudo()
        self.__data_envio = datetime.now()

    def visualizar(self):
        print("Notificação:")
        print(f"Data de envio: {self.__data_envio}")
        print(f"Conteúdo: {self.__conteudo}")
#quase