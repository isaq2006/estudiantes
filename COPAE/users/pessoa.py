from abc import ABC, abstractmethod
from os import system

class Pessoa(ABC):
    def __init__(self, id="", senha="", nome="", email="", fone="", nivelAcesso=""):
        self.__id = id
        self.__senha = senha
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        self.__nivelAcesso = nivelAcesso

    def get_id(self):
      return self.__id

    def get_senha(self):
      return self.__senha

    def get_nome(self):
      return self.__nome

    def get_email(self):
      return self.__email

    def get_fone(self):
      return self.__fone

    def get_nivelAcesso(self):
      return self.__nivelAcesso

    def set_id(self, id):
      self.__id= id
      
    def set_senha(self, senha):
      self.__senha = senha

    def set_nome(self, nome):
      self.__nome = nome

    def set_email(self, email):
      self.__email = email

    def set_fone(self, telefone):
      self.__fone = telefone

    def set_nivelAcesso(self,nivelAcesso):
      self.__nivelAcesso = nivelAcesso

    def definir_senha(self):
        while True:
            print("Digite uma senha:")
            senha = input()
            print("Confirme sua senha:")
            senhaConfirm = input()
            if senha == senhaConfirm:
                system("clear")
                print("Cadastro prosseguindo com sucesso")
                self.__senha = senha
                break
            else:
                system("claer")
                print("Senhas não conferem")
                print("Insira novamente sua senha")
                continue


    def get_imprimirDados(self):
        print(f"ID  {self.__id}")
        print(f"Senha: {self.__senha}")
        print(f"Nome: {self.__nome}")
        print(f"Email: {self.__email}")
        print(f"Fone: {self.__fone}")
        print(f"Nível de acesso: {self.__nivelAcesso}")


    def set_atualizarDados(self, bancoDeDados):
        id=self.get_id()
        if id in bancoDeDados:
            print("Deseja atualizar qual dado do seu cadastro?")
            print(f"1 Senha: {self.get_senha()}")
            print(f"2 Nome: {self.get_nome()}")
            print(f"3 Email: {self.get_email()}")
            print(f"4 Telefone: {self.get_fone()}")
            while True:
              decAtualize = int(input("Digite o número do atributo que deseja atualizar: "))
              novo_valor = input(f"Digite o novo valor: ")
              if decAtualize == 1:
                  self.set_senha(novo_valor)
                  break
              elif decAtualize == 2:
                  self.set_nome(novo_valor)
                  break
              elif decAtualize == 3:
                  self.set_email(novo_valor)
                  break
              elif decAtualize == 4:
                  self.set_fone(novo_valor)
                  break
              else:
                  print("Opção inválida")
                  continue

        else:
            print("Usuário não encontrado")

    def set_cadastro(self, bancoDeDados):
        system("clear")
        print("Insira seu ID:")
        id = input()
        while id in bancoDeDados:
            print("ID já vinculado")
            while True:
                print("Deseja fazer login?")
                print("1 - Sim\n2 - Não\n")
                decisao1 = input()
                system("clear")
                if decisao1 == "1":
                    return self.get_login(bancoDeDados)
                elif decisao1 == "2":
                    print("O ID já está vinculado a outra conta!")
                    print("Acesse pelo login, ou insira um novo ID")
                    print("Aperte ENTER")
                    input()
                    return self.set_cadastro(bancoDeDados)
                else:
                    print("Alternativa inválida")
                    continue
        self.__id = id
        print("Agora vamos definir sua senha, aperte ENTER para continuar")
        input()
        system('clear')
        self.definir_senha()

    @classmethod
    def get_login(cls, pessoas):
        print("Insira seu ID (número identificador):")
        id = input()
        if id not in pessoas:
            print("Conta não encontrada! Aperte ENTER para voltarmos ao menu:")
            input()
            system("clear")
            return False
        else:
            pessoa = pessoas.get(id)
            print("Insira sua senha:")
            senha = input()
            if pessoa.get_senha() != senha:
                print("Senha incorreta! Aperte ENTER para tentar novamente:")
                input()
                system("clear")
                return cls.get_login(pessoas)
            else:
                print("Login realizado com sucesso! Seja bem-vindo!")
                print("Aperte ENTER para finalizar")
                input()
                return True
#quase  

