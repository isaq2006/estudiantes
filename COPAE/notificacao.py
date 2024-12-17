from datetime import datetime

class Notificacao:
    def __init__(self, mensagem=None):
        # A inicialização da notificação recebe opcionalmente um objeto do tipo Mensagem.
        # Se uma mensagem é fornecida, extrai-se seu conteúdo para a notificação.
        # A data de envio da notificação é registrada com o momento atual.
        self.__conteudo = mensagem
        self.__data_envio = datetime.now()

    def visualizar(self):
        # Exibe os detalhes da notificação, incluindo a data de envio e o conteúdo.
        print("Notificação:")
        print(f"Data de envio: {self.__data_envio}")
        print(f"Conteúdo: {self.__conteudo}")

    def set_notificacao(self, conteudo):
        # Define ou atualiza o conteúdo da notificação com o valor passado.
        self.__conteudo = conteudo
