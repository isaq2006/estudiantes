from datetime import datetime

class Mensagem:
    def __init__(self, autor, conteudo,):
        self.__autor = autor
        self.__conteudo = conteudo
        self.__hora_envio = datetime.now()
        
    
    def get_conteudo(self):
        return self.__conteudo  

    def get_autor(self):
        return self.__autor
    
    def get_hora_envio(self):
        return self.__hora_envio
    
    def responder_mensagem(self, autor, mensagem):
        resposta = Mensagem(autor, input("Digite sua resposta: "))
        if not resposta:
            raise ValueError("A resposta não pode ser nula.")
        else:
        # Lógica para responder a mensagem
            mensagem += "\nResposta: " + resposta.set__conteudo()
            print("Mensagem respondida com sucesso.")

    def encaminhar(self, destinatario):
        if not self.__conteudo:
            raise ValueError("A mensagem não pode ser nula.")
        if not destinatario:
            raise ValueError("Destinatário inválido.")
        else:
            mensagem_encaminhada = Mensagem(self.get_autor(), self.get_conteudo())
            destinatario.receber_mensagem(mensagem_encaminhada)
            print("Mensagem encaminhada com sucesso.")

    def exibir_mensagem(self):
        print(f"Mensagem de {self.__autor} as {self.__hora_envio}")
        print(f"{self.__conteudo}")
        
    