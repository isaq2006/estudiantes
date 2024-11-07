# Importação da classe base Usuario
from users.usuario import Usuario

# Definição da classe Membro, que herda de Usuario
class Membro(Usuario):
    def __init__(self, id="", senha="", nome="", email="", fone="", nivelAcesso="", interesses="", habilidades="", clube=None):
        # Chama o construtor da classe pai (Usuario) para inicializar atributos herdados
        super().__init__(id, senha, nome, email, fone, nivelAcesso, interesses)
        # Atributo para armazenar as habilidades do membro
        self.__habilidades = habilidades
        # Associação com a classe Clube, que representa o clube ao qual o membro pertence
        self.__clubeAssociado = clube

    # Define as habilidades do membro
    def set_habilidades(self, habilidade):
        self.__habilidades = habilidade

    # Associa o membro a um clube específico
    def set_ClubeAssociado(self, clube):
        self.__clubeAssociado = clube

    # Imprime dados do membro, incluindo os dados herdados e o nível de habilidades
    def get_imprimirDados(self):
        super().get_imprimirDados()  # Chama o método da classe pai para imprimir os dados básicos
        print(f"Nível de habilidades: {self.__habilidades}")  # Exibe o nível de habilidades específico do membro

    # Realiza o cadastro do membro, solicitando dados adicionais e adicionando ao banco de dados
    def set_cadastro(self, bancoDeDados):
        # Chama o método de cadastro da classe pai
        super().set_cadastro(bancoDeDados)
        print("Dados necessários para um MEMBRO de clube")
        print("Qual seu nível de habilidade? Insira-o:")
        self.__habilidades = input()  # Recebe o nível de habilidade do usuário
        self.set_nivelAcesso("limitado ao clube")  # Define o nível de acesso específico para um membro
        bancoDeDados[self.get_id()] = self  # Adiciona o membro ao banco de dados

    # Métodos de mensagem herdados da classe Usuario
    def enviarMensagem(self):
        super().enviarMensagem()  # Envia uma mensagem usando o método da classe pai

    def excluirMensagem(self, mensagem):
        super().excluirMensagem(mensagem)  # Exclui uma mensagem usando o método da classe pai

    # Permite que o membro visualize todos os clubes disponíveis
    def visualizarClubes(self, clubes):
        super().visualizarClubes(clubes)  # Usa o método da classe pai para exibir os clubes

    # Permite que o membro adira a uma comunidade ou clube específico
    def aderirComunidade(self, clubes):
        super().aderirComunidade(clubes)  # Chama o método da classe pai para aderir a um clube

    # Retorna o nível de acesso do membro
    def get_nivelAcesso(self):
        return super().get_nivelAcesso()  # Utiliza o método da classe pai para retornar o nível de acesso

    # Envia uma atividade para o clube associado; mostra uma relação de associação com a classe Atividade através de Clube
    def enviarAtividade(self, atividade):
        # Associa a atividade ao clube ao qual o membro pertence
        self.__clubeAssociado.set_atividade(atividade)

    # Permite editar atividades dentro do clube associado
    def editarAtividade(self):
        self.__clubeAssociado.editarAtividade()

    # Retorna o clube ao qual o membro está associado
    def get_clubeAsssociado(self):
        return self.__clubeAssociado
