# Importa o módulo uuid para gerar IDs únicos para cada instância de Chat
import uuid

# Definição da classe Chat
class Chat:
    def __init__(self, mensagens=None):
        # Inicializa o chat com um ID único e uma lista de mensagens
        self.__id = uuid.uuid4()  # Gera um ID único para cada chat
        self.__mensagens = []# Inicializa a lista de mensagens como vazia, se não for fornecida

    # Método para obter a lista de mensagens do chat
    def get_mensagens(self):
        return self.__mensagens  # Retorna a lista de mensagens armazenadas

    # Método para enviar uma mensagem ao chat
    def send_mensage(self, mensagem):
        # Adiciona a nova mensagem à lista de mensagens
        self.__mensagens.append(mensagem)

    # Método para exibir todas as mensagens do chat
    def exibir_mensagens(self):
        # Percorre e exibe cada mensagem na lista de mensagens
        for mensagem in self.__mensagens:
            mensagem.exibir_mensagem()  # Chama o método exibir_mensagem de cada objeto mensagem
