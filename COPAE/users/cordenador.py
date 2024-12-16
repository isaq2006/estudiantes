# Importação da classe base Usuario
from users.usuario import Usuario
from os import system
# Definição da classe Coordenador, que herda de Usuario
class Coordenador(Usuario):
    def __init__(self, id="", senha="", nome="", email="", fone="", nivelAcesso="", interesses="", conhecimentoTecnico="", experiencia="", clubeCordenando=None):
        # Chama o construtor da classe pai (Usuario) para inicializar atributos herdados
        super().__init__(id, senha, nome, email, fone, nivelAcesso, interesses)
        # Atributos específicos do Coordenador, incluindo conhecimento técnico, experiência e o clube que coordena
        self.__conhecimentoTecnico = conhecimentoTecnico
        self.__experiencia = experiencia
        # Associação com a classe Clube, indicando o clube que o coordenador está gerenciando
        self.__clubeCordenando = clubeCordenando

    # Imprime dados do coordenador, incluindo conhecimento técnico e experiência
    def get_imprimirDados(self, bancoDeDados):
        super().get_imprimirDados(bancoDeDados)  # Chama o método da classe pai para imprimir os dados básicos
        print(f"Conhecimento técnico: {self.__conhecimentoTecnico}")
        print(f"Experiência: {self.__experiencia}")

    # Realiza o cadastro do coordenador, solicitando dados adicionais específicos
    def set_cadastro(self, bancoDeDados):
        super().set_cadastro(bancoDeDados)  # Chama o método de cadastro da classe pai
        print("Quais são seus conhecimentos técnicos? Insira-os:")
        self.__conhecimentoTecnico = input()  # Recebe o conhecimento técnico do coordenador
        print("Qual sua experiência nessa área? Insira-a:")
        self.__experiencia = input()  # Recebe a experiência do coordenador
        self.set_nivelAcesso("ilimitado no clube")  # Define o nível de acesso específico para o coordenador
        bancoDeDados[self.get_id()] = self  # Adiciona o coordenador ao banco de dados

    # Retorna o nível de acesso do coordenador
    def get_nivelAcesso(self):
        return super().get_nivelAcesso()  # Utiliza o método da classe pai para retornar o nível de acesso
    
    def set_conhecimentoTecnico(self, conhecimentoTecnico):
        self.__conhecimentoTecnico = conhecimentoTecnico 
        
    def set_experiencia(self, experiencia):
        self.__experiencia = experiencia
        
    def set_clube(self, clubeCordenando):
        self.__clubeCordenando = clubeCordenando

    # Métodos de mensagem herdados da classe Usuario
    def enviarMensagem(self):
        super().enviarMensagem()  # Envia uma mensagem usando o método da classe pai

    def excluirMensagem(self, mensagem):
        super().excluirMensagem(mensagem)  # Exclui uma mensagem usando o método da classe pai

    # Permite que o coordenador visualize todos os clubes disponíveis
    def visualizarClubes(self, clubes):
        super().visualizarClubes(clubes)  # Usa o método da classe pai para exibir os clubes

    # Permite que o coordenador adira a uma comunidade ou clube específico
    def aderirComunidade(self, clubes):
        super().aderirComunidade(clubes)  # Chama o método da classe pai para aderir a um clube

    # Cria um novo clube, que será gerenciado pelo próprio coordenador
    def criar_clube(self):
        # Lógica para criar um novo clube
        import clube
        system("clear")
        print("Bem-vindo à aba de criação!!!")
        novoClube = clube.Clube()
        novoClube.set_cordenador = self  # Associa o coordenador ao clube criado
        print("Digite o nome do clube:")
        novoClube.set_nome = input()  # Define o nome do clube
        print("Dê a descrição do mesmo:")
        novoClube.set_descricao = input()  # Define a descrição do clube
        system("clear")
        print("Clube criado com sucesso!!!")
        self.__clubeCordenando = novoClube  # Atribui o novo clube ao coordenador

        return novoClube

    # Exclui o clube que o coordenador está gerenciando
    def excluir_clube(self, clubes):
        # Lógica para excluir o clube
        for clube in clubes:
            if clube.get_cordenador() == self:
                clubes.remove(clube) 
        del self
        return clubes# Remove o clube do coordenador e exclui o coordenador

    # Adiciona um novo membro ao clube gerenciado pelo coordenador
    # Cria uma relação de agregação de membros ao clube
    def adicionar_membro(self, bancoDeDados):
        # Lógica para adicionar um novo membro ao clube
        if len(bancoDeDados) < 2:
            print("não existem outras pessoas cadastradas!!!")
            pass
        from .membro import Membro
        # Lista os usuários disponíveis no banco de dados para o coordenador selecionar
        print("usuarios cadastrados no sistema:")
        for i, usuario in enumerate(bancoDeDados, 1):
            print(f"Usuario {i}: {usuario.get_nome()}")
        print("\nDigite o número do usuário que você deseja adicionar:")
        escolha = int(input())
        listaBanco = list(bancoDeDados)
        if 1 <= escolha <= len(listaBanco):
            usuarioEscolhido = listaBanco[escolha - 1]
        
        # Cria um novo membro e associa como uma agregação ao clube do coordenador
        novoMembro = Membro()
        novoMembro.set_id(usuarioEscolhido.get_id())
        novoMembro.set_senha(usuarioEscolhido.get_senha())
        novoMembro.set_nome(usuarioEscolhido.get_nome())
        novoMembro.set_email(usuarioEscolhido.get_email())
        novoMembro.set_fone(usuarioEscolhido.get_fone())
        novoMembro.set_nivelAcesso(usuarioEscolhido.get_nivelAcesso())
        novoMembro.set_hobbies("nenhuma definida")
        novoMembro.set_ClubeAssociado(self.__clubeCordenando)  # Associa o novo membro ao clube do coordenador
        self.__clubeCordenando.set_membros(novoMembro)  # Adiciona o membro ao clube
        print(f"O membro {novoMembro.get_nome()} foi adicionado com sucesso!")

    # Remove um membro específico do clube gerenciado pelo coordenador
    def remover_membro(self):
        # Lógica para remover um membro do clube
        membros = self.__clubeCordenando.get_membros()
        print("Membros:")
        if not membros:
            print("Nenhum membro encontrado")
            pass
        # Exibe a lista de membros para o coordenador escolher qual remover
        for i, membro in enumerate(membros, 1):
            print(f"{i}. {membro.get_nome()}")
        escolha = int(input("\nDigite o número do membro que deseja remover: "))
        if 1 <= escolha <= len(membros):
            membro_escolhido = membros[escolha - 1]
            self.__clubeCordenando.get_membros().remove(membro_escolhido)  # Remove o membro do clube
            print(f"O membro {membro_escolhido.get_nome()} foi removido com sucesso!")

    # Cria uma nova atividade no clube gerenciado pelo coordenador
    # Cria uma associação de agrgação de atividades ao clube
    def criar_atividade(self):
        # Lógica para criar uma nova atividade
        from atividade import Atividade
        novaAtividade = Atividade()
        novaAtividade.set_titulo(input("Digite o título da atividade: "))
        novaAtividade.set_descricao(input("Digite a descrição da atividade: "))
        novaAtividade.set_data_vencimento(input("Digite a data de vencimento da atividade (formato: YYYY-MM-DD): "))
        novaAtividade.set_tipo_arquivo(input("Digite o tipo de arquivo aceito pela atividade: "))
        
        # Adiciona a nova atividade ao clube do coordenador estabelecendo a agregação
        self.__clubeCordenando.set_atividades(novaAtividade)
        print(f"A atividade {novaAtividade.get_titulo()} foi criada com sucesso!")

    # Exclui uma atividade específica do clube gerenciado pelo coordenador
    def excluir_atividade(self):
        atividades = self.__clubeCordenando.get_atividades()
        if not atividades:
            print("Nenhuma atividade encontrada")
            
        # Exibe a lista de atividades para o coordenador escolher qual excluir
        print("Atividades:")
        for i, atividade in enumerate(atividades, 1):
            print(f"{i}°. {atividade.get_titulo()}")
        
        escolha = int(input("Digite o número da atividade que deseja excluir: "))
        if 1 <= escolha <= len(atividades):
            atividade_escolhida = atividades[escolha - 1]
            self.__clubeCordenando.set_atividades(atividade_escolhida)  # Remove a atividade do clube
            print(f"A atividade {atividade_escolhida.get_titulo()} foi excluída com sucesso!")
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

    # Retorna o clube que o coordenador está gerenciando
    def get_clubeCordenando(self):
        return self.__clubeCordenando
    
    def get_nome(self):
        return super().get_nome()