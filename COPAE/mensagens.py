from datetime import datetime

class Mensagem:
    def __init__(self, autor, conteudo):
        # O autor e o conteúdo são inicializados ao criar uma nova mensagem.
        # Além disso, a hora de envio é registrada com o momento atual.
        self.__autor = autor
        self.__conteudo = conteudo
        self.__hora_envio = datetime.now()

    def get_conteudo(self):
        # Retorna o conteúdo da mensagem.
        return self.__conteudo  

    def get_autor(self):
        # Retorna o autor da mensagem.
        return self.__autor

    def get_hora_envio(self):
        # Retorna a hora de envio da mensagem.
        return self.__hora_envio
    
    # Setters
    def set_conteudo(self, novo_conteudo):
        # Define um novo conteúdo para a mensagem.
        self.__conteudo = novo_conteudo

    def set_autores(self, novo_autor):
        # Define um novo autor para a mensagem.
        self.__autor = novo_autor

    def set_hora_envio(self, nova_hora):
        # Define uma nova hora de envio para a mensagem.
        self.__hora_envio = nova_hora

    def responder_mensagem(self, autor, mensagem):
        # Cria uma resposta para a mensagem original.
        # A resposta é uma nova instância da classe Mensagem, 
        # que recebe o autor e o conteúdo da resposta.
        resposta = Mensagem(autor, input("Digite sua resposta: "))
        if not resposta:
            raise ValueError("A resposta não pode ser nula.")
        else:
            # Lógica para responder a mensagem, concatenando a resposta
            # ao conteúdo da mensagem original.
            mensagem += "\nResposta: " + resposta.get_conteudo()
            print("Mensagem respondida com sucesso.")

    def encaminhar(self, destinatario):
        # Envia a mensagem para um destinatário.
        # Cria uma nova instância da classe Mensagem com o conteúdo original,
        # e encaminha para o destinatário fornecido.
        if not self.__conteudo:
            raise ValueError("A mensagem não pode ser nula.")
        if not destinatario:
            raise ValueError("Destinatário inválido.")
        else:
            # Criação de uma nova instância de Mensagem para encaminhar ao destinatário
            mensagem_encaminhada = Mensagem(self.get_autor(), self.get_conteudo())
            # Chamando o método 'receber_mensagem' do destinatário para processar o recebimento.
            destinatario.receber_mensagem(mensagem_encaminhada)
            print("Mensagem encaminhada com sucesso.")

    def exibir_mensagem(self):
        # Exibe a mensagem com informações sobre o autor, hora de envio e conteúdo.
        print(f"Mensagem de {self.__autor} as {self.__hora_envio}")
        print(f"{self.__conteudo}")
