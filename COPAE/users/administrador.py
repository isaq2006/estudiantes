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

    def removerUsuario(self, bancoDeDados):
        # Método para visualizar e remover membros
        while True:
            print("\n--- Lista de Usuários ---")
            # Listando os membros do dicionário
            for chave, usuario in bancoDeDados.items():
                print(f"Usuário {chave}: {usuario.get_nome()}")
            
            # Solicita ao usuário qual membro remover
            try:
                numero = input("\nDigite o número do usuário que deseja remover (ou 0 para sair): ")
                
                if numero == "0":
                    print("Saindo...")
                    return bancoDeDados
                
                # Verifica se a chave existe no banco de dados
                if numero in bancoDeDados:
                    del bancoDeDados[numero]  # Remove o usuário pela chave
                    print("Membro removido com sucesso!")
                    return bancoDeDados
                else:
                    print("Número inválido. Nenhum membro foi removido.")
            except ValueError:
                print("Entrada inválida. Digite apenas números inteiros.")
                
    def removerClube(self, bancoDeDados):
        while True:
            # Exibe a lista de clubes com índices numerados
            print("\n--- Lista de Clubes ---")
            for i, clube in enumerate(bancoDeDados, 1):
                print(f"Clube {i}: {clube.get_nome()}")  # Mostra os clubes numerados a partir de 1

            # Entrada do usuário para selecionar o clube
            try:
                numero = int(input("\nDigite o número do clube que deseja remover (ou 0 para sair): "))
                
                if numero == 0:
                    print("Saindo ...")
                    return bancoDeDados
                
                # Verifica se o número está dentro do intervalo válido
                if 1 <= numero <= len(bancoDeDados):
                    del bancoDeDados[numero - 1]  # Remove o clube (convertendo para índice da lista)
                    print("Clube removido com sucesso!")
                    return bancoDeDados
                else:
                    print("Número inválido. Nenhum clube foi removido.")
            
            except ValueError:
                print("Entrada inválida. Digite apenas números inteiros.")