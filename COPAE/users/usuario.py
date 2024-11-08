# Importação da classe base Pessoa
from users.pessoa import Pessoa

# Classe Usuario herda de Pessoa (Herança)
class Usuario(Pessoa):
    def __init__(self, id="", senha="", nome="", email="", fone="", nivelAcesso="", hobbies=""):
        # Chamada ao construtor da classe Pessoa para inicializar atributos comuns (Herança)
        super().__init__(id, senha, nome, email, fone, nivelAcesso)
        
        # Definindo um atributo específico da classe Usuario
        self.__hobbies = hobbies

    # Método para imprimir dados do usuário, incluindo hobbies
    def get_imprimirDados(self):
        # Chamada ao método herdado de Pessoa para imprimir dados básicos
        super().get_imprimirDados()
        print(f"Hobbies: {self.__hobbies}")

    # Método para cadastrar usuário no banco de dados
    def set_cadastro(self, bancoDeDados):
        # Chamada ao método herdado de Pessoa para procedimentos comuns de cadastro
        super().set_cadastro(bancoDeDados)
        
        print("Insira seu nome de Usuário:")
        self.set_nome(input())  # Seta o nome do usuário
        print("Insira seu email:")
        self.set_email(input())  # Seta o email do usuário
        print("Insira seu telefone:")
        self.set_fone(input())   # Seta o telefone do usuário
        print("Quais são seus interesses? Insira-os:")
        self.__hobbies = input() # Seta os hobbies específicos do usuário
        self.set_nivelAcesso("área inicial")  # Define um nível de acesso inicial

    # Método para obter o nível de acesso do usuário, herdado de Pessoa
    def get_nivelAcesso(self):
        return super().get_nivelAcesso()
    def set_hobbies(self, hobbies):
        self.__hobbies = hobbies

    # Associação com a classe Mensagem para enviar mensagens
    def enviarMensagem(self):
        # Importação da classe Mensagem para criar uma mensagem
        from ..mensagens import Mensagem
        print("Digite seu texto abaixo")
        
        # Criação de uma instância de Mensagem, associando o remetente (nome do usuário) ao conteúdo
        mensagem = Mensagem(self.get_nome(), input())
        from ..notificacao import Notificacao
        # Criação de uma instância de Notificação associando a mensagem e ao conteúdo
        notificar = Notificacao()
        notificar.set_notificacao(mensagem.get_conteudo())
        notificar.visualizar()
        return mensagem

    # Método para excluir uma mensagem, assumindo que `mensagem` é um objeto da classe Mensagem
    def excluirMensagem(self, mensagem):
        del mensagem  # Exclui o objeto de mensagem passado como parâmetro

    # Método para receber uma mensagem, exibindo o conteúdo enviado
    def receber_mensagem(self, mensagem):
        print(mensagem.get_conteudo())  # Exibe o conteúdo da mensagem recebida

    # Método para aderir a uma comunidade, com possibilidade de criar ou participar de um clube
    def aderirComunidade(self, bancoDeDados):
        while True:
            print("Você deseja se inscrever ou criar um clube?")
            print("[1] Criar um clube")
            print("[2] Participar de um clube")
            opcao = input()
            
            # Opção para criar um clube
            if opcao == "1":
                # Associação com a classe Coordenador para criar um novo clube
                from .cordenador import Coordenador
                cordenador = Coordenador()
                cordenador.set_cadastro(bancoDeDados)  # Cadastro do coordenador
                return cordenador
            
            # Opção para participar de um clube
            elif opcao == "2":
                # Associação com a classe Membro para se inscrever em um clube existente
                from .membro import Membro
                membro = Membro()
                membro.set_cadastro(bancoDeDados)  # Cadastro do membro
                return membro
            
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")

    # Método para visualizar clubes e seus coordenadores
    def visualizarClubes(self, clubes):
        if not clubes:
            print("Não esxistem clubes cadastrados no momento!!!")
        else:
            for clube in clubes:
                # Exibição dos dados de cada clube
                print(f"Nome: {clube.get_nome()}")
                print(f"Descrição: {clube.get_descricao()}")
                # Associação com a classe Coordenador ao exibir o coordenador de cada clube
                print(f"Cordenador: {clube.get_cordenador().get_nome()}")
                print("\n")
