from usuario import Usuario

class Membro(Usuario):
    def __init__(self, id="", senha="", nome="", email="", fone="", nivelAcesso="", interesses="", habilidades="", clube=None):
        super().__init__(id, senha, nome, email, fone, nivelAcesso, interesses)
        self.__habilidades = habilidades
        self.__clubeAssociado = clube
        
    def set_habilidades(self,habilidade):
        self.__habilidades=habilidade
        
    def set_ClubeAssociado(self,clube):
        self.__clubeAssociado= clube

    def get_imprimirDados(self):
        super().get_imprimirDados()
        print(f"Nível de habilidades: {self.__habilidades}")

    def set_cadastro(self, bancoDeDados):
        super().set_cadastro(bancoDeDados)
        print("Dados necessários para um MEMBRO de clube")
        print("Qual seu nível de habilidade? Insira-o:")
        self.__habilidades = input()
        self.set_nivelAcesso("limitado ao clube")
        bancoDeDados[self.get_id()] = self
        
    def enviarMensagem(self):
        super().enviarMensagem()
        
    def excluirMensagem(self, mensagem):
        super().excluirMensagem(mensagem)

    def visualizarClubes(self, clubes):
        super().visualizarClubes(clubes)
        
    def aderirComunidade(self, clubes):
        super().aderirComunidade(clubes)

    #aqui vemos a relação de associação com a classe Atividade através dá classe Clube
    def enviarAtividade(self):
        self.clubeAssociado.enviarAtividade()