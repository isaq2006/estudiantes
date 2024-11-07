from users.pessoa import Pessoa

class Usuario(Pessoa):
    def __init__(self, id="", senha="", nome="", email="", fone="", nivelAcesso="", hobbies=""):
        super().__init__(id, senha, nome, email, fone, nivelAcesso)
        self.__hobbies = hobbies

    def get_imprimirDados(self):
        super().get_imprimirDados()
        print(f"Hobbies: {self.__hobbies}")

    def set_cadastro(self, bancoDeDados):
        super().set_cadastro(bancoDeDados)
        print("Cadastro de USUÁRIO")
        print("insira seu nome de Usuário:")
        self.set_nome(input())
        print("insira seu email:")
        self.set_email(input())
        print("insira seu telefone:")
        self.set_fone(input())
        print("Quais são seus interesses? Insira-os:")
        self.__hobbies = input()
        self.set_nivelAcesso("área inicial")
        
    def get_nivelAcesso(self):
        return super().get_nivelAcesso()
    # associação com a classe mensagem
    def enviarMensagem(self):
        from ..mensagens import Mensagem
        print("Digite seu texto abaixo")
        mensagem = Mensagem(self.get_nome(), input())
        return mensagem
        
    def excluirMensagem(self, mensagem):
        del mensagem 
        
    def receber_mensagem(self, mensagem):
        print(mensagem.get_conteudo())
        
    def aderirComunidade(self, bancoDeDados):
        while True:
            print("voce deseja se inscrever ou criar um clube?")
            print("[1] Criar um clube")
            print("[2] Participar de um clube")
            opcao = input()
            if opcao == "1":
                from .cordenador import Coordenador
                cordenador = Coordenador()
                cordenador.set_cadastro(bancoDeDados)
                return cordenador
            elif opcao == "2":
                from .membro import Membro
                membro = Membro()
                membro.set_cadastro(bancoDeDados)
                return membro
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
            
    def visualizarClubes(self, clubes):
        for clube in clubes:
            print(f"Nome: {clube.get_nome()}")
            print(f"Descrição: {clube.get_descricao()}")
            print(f"Cordenador: {clube.get_cordenador().get_nome()}")
            print("\n")
            