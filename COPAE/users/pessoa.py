from abc import ABC, abstractmethod  # ABC e abstractmethod são usados para criar classes abstratas e métodos abstratos
from os import system  # Importação para manipular o terminal (limpeza de tela)

# Definição da classe abstrata Pessoa
class Pessoa(ABC):
    def __init__(self, id="", senha="", nome="", email="", fone="", nivelAcesso=""):
        # Inicialização dos atributos privados da classe Pessoa
        self.__id = id
        self.__senha = senha
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        self.__nivelAcesso = nivelAcesso

    # Métodos "getters" para acessar os atributos privados da classe
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

    # Métodos "setters" para modificar os atributos privados da classe
    def set_id(self, id):
        self.__id = id

    def set_senha(self, senha):
        self.__senha = senha

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_fone(self, telefone):
        self.__fone = telefone

    def set_nivelAcesso(self, nivelAcesso):
        self.__nivelAcesso = nivelAcesso

    # Método para definir a senha do usuário
    def definir_senha(self):
        # Este método permite ao usuário definir uma senha e confirmá-la
        while True:
            try:
                print("Digite uma senha:")
                senha = input()
                print("Confirme sua senha:")
                senhaConfirm = input()
                if senha == senhaConfirm:
                    system("clear")
                    print("Cadastro prosseguindo com sucesso")
                    self.__senha = senha  # Senha confirmada e salva
                    break
                else:
                    system("clear")
                    print("Senhas não conferem. Tente novamente.")
                    continue
            except Exception as e:
                print(f"Ocorreu um erro ao definir a senha: {e}. Tente novamente.")
            finally:
                # O `finally` é sempre executado, independentemente de erro ou sucesso
                print("Tentativa de definir senha concluída.")  # Mensagem informativa

    # Método para imprimir os dados da pessoa
    def get_imprimirDados(self):
        # Exibe todos os atributos privados da classe Pessoa
        print(f"ID  {self.__id}")
        print(f"Senha: {self.__senha}")
        print(f"Nome: {self.__nome}")
        print(f"Email: {self.__email}")
        print(f"Fone: {self.__fone}")
        print(f"Nível de acesso: {self.__nivelAcesso}")

    # Método para atualizar dados de cadastro de um usuário já existente
    def set_atualizarDados(self, bancoDeDados):
        # Verifica se o ID existe no banco de dados
        id = self.get_id()
        if id in bancoDeDados:
            print("Deseja atualizar qual dado do seu cadastro?")
            print(f"1 Senha: {self.get_senha()}")
            print(f"2 Nome: {self.get_nome()}")
            print(f"3 Email: {self.get_email()}")
            print(f"4 Telefone: {self.get_fone()}")
            while True:
                try:
                    # Usuário escolhe qual atributo deseja atualizar
                    decAtualize = int(input("Digite o número do atributo que deseja atualizar: "))
                    if decAtualize == 1:
                        self.set_senha(input("Digite a nova senha: "))  # Atualiza a senha
                        break
                    elif decAtualize == 2:
                        self.set_nome(input("Digite o novo nome: "))  # Atualiza o nome
                        break
                    elif decAtualize == 3:
                        self.set_email(input("Digite o novo email: "))  # Atualiza o email
                        break
                    elif decAtualize == 4:
                        self.set_fone(input("Digite o novo telefone: "))  # Atualiza o telefone
                        break
                    else:
                        print("Opção inválida. Tente novamente.")
                        continue
                except ValueError:
                    print("Por favor, insira um número válido.")
                    continue
                except Exception as e:
                    print(f"Ocorreu um erro ao atualizar os dados: {e}. Tente novamente.")
                finally:
                    # O `finally` é sempre executado, mesmo com erro ou sucesso
                    print("Tentativa de atualização concluída.")

        else:
            print("Usuário não encontrado.")

    # Método de cadastro de um novo usuário
    def set_cadastro(self, bancoDeDados):
        system("clear")
        try:
            print("Insira seu ID:")
            id = input()

            # Verifica se o ID já está cadastrado no banco de dados
            while id in bancoDeDados:
                print("ID já vinculado.")
                print("Deseja fazer login?")
                print("1 - Sim\n2 - Não")
                decisao1 = input()
                system("clear")
                if decisao1 == "1":
                    # Chama o método de login caso o ID já esteja vinculado
                    return self.get_login(bancoDeDados)
                elif decisao1 == "2":
                    print("O ID já está vinculado a outra conta!")
                    print("Acesse pelo login ou insira um novo ID.")
                    input("Pressione ENTER para tentar novamente.")
                    return self.set_cadastro(bancoDeDados)
                else:
                    print("Alternativa inválida. Tente novamente.")
                    continue

            self.__id = id  # Define o ID após verificar que ele é único
            print("Agora vamos definir sua senha, aperte ENTER para continuar")
            input()
            system('clear')
            self.definir_senha()  # Chama o método para definir a senha
            print("Insira seu nome de Usuário:")
            self.set_nome(input())  # Seta o nome do usuário
            print("Insira seu email:")
            self.set_email(input())  # Seta o email do usuário
            print("Insira seu telefone:")
            self.set_fone(input())  # Seta o telefone do usuário

        except Exception as e:
            print(f"Ocorreu um erro durante o cadastro: {e}. Tente novamente.")
        finally:
            # O `finally` é sempre executado, independentemente de erro ou sucesso
            print("Cadastro tentado. Finalizando processo de cadastro.")

    # Método de login de um usuário usando o ID e a senha
    @classmethod
    def get_login(cls, pessoas):
        try:
            print("Insira seu ID (número identificador):")
            id = input()

            # Verifica se o ID está presente no banco de dados
            if id not in pessoas:
                print("Conta não encontrada! Aperte ENTER para voltarmos ao menu:")
                input()
                system("clear")
                return False
            else:
                pessoa = pessoas.get(id)
                print("Insira sua senha:")
                senha = input()

                # Verifica a senha do usuário
                if pessoa.get_senha() != senha:
                    print("Senha incorreta! Aperte ENTER para tentar novamente.")
                    input()
                    system("clear")
                    return cls.get_login(pessoas)
                else:
                    print("Login realizado com sucesso! Seja bem-vindo!")
                    input("Aperte ENTER para finalizar.")
                    return True  # Login bem-sucedido
        except Exception as e:
            print(f"Ocorreu um erro no login: {e}. Tente novamente.")
            return False
        finally:
            # O `finally` é sempre executado, independentemente do que aconteceu no `try` ou `except`
            print("Processo de login finalizado.")