from pessoa import Pessoa

class Administrador(Pessoa):
    def __init__(self, id="", senha="", nome="", email="", fone="", nivelAcesso="", cargoInstituinte=""):
        super().__init__(id, senha, nome, email, fone, nivelAcesso)
        self.__cargoInstituinte = cargoInstituinte

    def get_imprimirDados(self):
        super().get_imprimirDados()
        print(f"Cargo do Instituinte: {self.__cargoInstituinte}")

    def set_cadastro(self, bancoDeDados):
        super().set_cadastro(bancoDeDados)
        print("cadastro de ADMINISTRADOR")
        print("insira seu nome de Usuário:")
        self.set_nome(input())
        print("insira seu email:")
        self.set_email(input())
        print("insira seu telefone:")
        self.set_fone(input())
        print("insira seu cargo na Instituição:")
        self.__cargoInstituinte = input()
        self.set_nivelAcesso("ilimitado")
