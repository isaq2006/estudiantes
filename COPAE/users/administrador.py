# Importação da classe base Pessoa
from users.pessoa import Pessoa

# Definição da classe Administrador, que herda de Pessoa
class Administrador(Pessoa):
    def __init__(self, id="", senha="", nome="", email="", fone="", nivelAcesso="", cargoInstituinte=""):
        # Chama o construtor da classe pai (Pessoa) para inicializar atributos herdados
        super().__init__(id, senha, nome, email, fone, nivelAcesso)
        # Atributo específico do Administrador que representa o cargo na instituição
        self.__cargoInstituinte = cargoInstituinte

    # Método para imprimir os dados do administrador
    def get_imprimirDados(self):
        super().get_imprimirDados()  # Chama o método da classe pai para exibir os dados básicos
        print(f"Cargo do Instituinte: {self.__cargoInstituinte}")  # Exibe o cargo do administrador

    # Realiza o cadastro do administrador, solicitando informações adicionais específicas
    def set_cadastro(self, bancoDeDados):
        super().set_cadastro(bancoDeDados)  # Chama o método de cadastro da classe pai
        print("Cadastro de ADMINISTRADOR")
        print("Insira seu nome de Usuário:")
        self.set_nome(input())  # Recebe o nome do administrador
        print("Insira seu email:")
        self.set_email(input())  # Recebe o email do administrador
        print("Insira seu telefone:")
        self.set_fone(input())  # Recebe o telefone do administrador
        print("Insira seu cargo na Instituição:")
        self.__cargoInstituinte = input()  # Recebe o cargo do administrador na instituição
        self.set_nivelAcesso("ilimitado")  # Define o nível de acesso como ilimitado para o administrador

    # Retorna o nível de acesso do administrador
    def get_nivelAcesso(self):
        return super().get_nivelAcesso()  # Usa o método da classe pai para retornar o nível de acesso
