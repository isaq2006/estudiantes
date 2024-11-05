from users.usuario import Usuario

class Coordenador(Usuario):
    def __init__(self, id="", senha="", nome="", email="", fone="", nivelAcesso="", interesses="", conhecimentoTecnico="", experiencia="",clubeCordenando=None):
        super().__init__(id, senha, nome, email, fone, nivelAcesso, interesses)
        self.__conhecimentoTecnico = conhecimentoTecnico
        self.__experiencia = experiencia
        self.__clubeCordenando = clubeCordenando

    def get_imprimirDados(self, bancoDeDados):
        super().get_imprimirDados(bancoDeDados)
        print(f"Conhecimento técnico: {self.__conhecimentoTecnico}")
        print(f"Experiência: {self.__experiencia}")
        
    def set_cadastro(self, bancoDeDados):
        super().set_cadastro(bancoDeDados)
        print("Dados necessários para um COORDENADOR")
        print("Quais são seus conhecimentos técnicos? Insira-os:")
        self.__conhecimentoTecnico = input()
        print("Qual sua experiência nessa área? Insira-a:")
        self.__experiencia = input()
        self.set_nivelAcesso("ilimitado no clube")
        bancoDeDados[self.get_id()] = self
        
    def enviarMensagem(self):
        super().enviarMensagem()
    
    def excluirMensagem(self, mensagem):
        super().excluirMensagem(mensagem)

    def visualizarClubes(self, clubes):
        super().visualizarClubes(clubes)
        
    def aderirComunidade(self, clubes):
        super().aderirComunidade(clubes)
        
    def criar_clube(self):
        # Lógica para criar um novo clube
        from ..clube import Clube
        novoClube= Clube()
        novoClube.set_cordenador=self
        print("Digite o nome do clume:")
        novoClube.set_nome=input()
        print("Dê a descrição do mesmo:")
        novoClube.set_descricao=input()
        print("clube criado com sucesso!!!")
        self.__clubeCordenando = novoClube
        
        return novoClube
        
    def excluir_clube(self):
        # Lógica para excluir o clube
        del self.__clubeCordenando, self

    def adicionar_membro(self, bancoDeDados):
        # Lógica para adicionar um novo membro ao clube
        from membro import Membro
        for i,usuario in enumerate(bancoDeDados,1):
           print(f"Usuario {i}: {usuario.get_nome()}")
        print("\nDigite a qual usuario você deseja adicionar:")
        escolha=int(input())
        if 1 <= escolha <= len(bancoDeDados):
                usuarioEscolhido= bancoDeDados[escolha - 1]  
        novoMembro=Membro()
        novoMembro.set_id(usuarioEscolhido.get_id())
        novoMembro.set_senha(usuarioEscolhido.get_senha())
        novoMembro.set_nome(usuarioEscolhido.get_nome())
        novoMembro.set_email(usuarioEscolhido.get_email())
        novoMembro.set_fone(usuarioEscolhido.get_fone())
        novoMembro.set_nivelAcesso(usuarioEscolhido.get_nivelAcesso())
        novoMembro.set_habilidades("nenhuma definida")
        novoMembro.set_clubeAssociado(self.__clubeCordenando)  
        self.__clubeCordenando.set_membros(novoMembro)
        print(f"O membro {novoMembro.get_nome()} foi adicionado com sucesso!")

    def remover_membro(self):
        # Lógica para remover um membro do clube
        membros = self.__clubeCordenando.get_membros()
        print("Membros:")
        if not membros:
            print("Nenhum membro encontrado")
            
        for i, membro in enumerate(membros, 1):
            print(f"{i}. {membro.get_nome()}")
        escolha = int(input("Digite o número do membro que deseja remover: "))
        if 1 <= escolha <= len(membros):
            membro_escolhido = membros[escolha - 1]
        self.__clubeCordenando.get_membros().remove(membro_escolhido)
        print(f"O membro {membro_escolhido.get_nome()} foi removido com sucesso!")

    def criar_atividade(self, atividade):
        # Lógica para criar uma nova atividade
        from atividade import Atividade
        novaAtividade = Atividade()
        novaAtividade.set_titulo(input("Digite o título da atividade: "))
        novaAtividade.set_descricao(input("Digite a descrição da atividade: "))
        novaAtividade.set_data_vencimento(input("Digite a data de vencimento da atividade (formato: YYYY-MM-DD): "))
        novaAtividade.set_tipo_arquivo(input("Digite o tipo de arquivo aceito pela atividade: "))
        
        self.__clubeCordenando.get_atividades().append(novaAtividade)
        print(f"A atividade {novaAtividade.get_titulo()} foi criada com sucesso!")

    def excluir_atividade(self):
        atividades = self.__clubeCordenando.get_atividades()
        if not atividades:
            print("Nenhuma atividade encontrada")
            
        print("Atividades:")
        for i, atividade in enumerate(atividades, 1):
            print(f"{i}. {atividade.get_titulo()}")
        
            escolha = int(input("Digite o número da atividade que deseja excluir: "))
            if 1 <= escolha <= len(atividades):
                atividade_escolhida = atividades[escolha - 1]
                self.__clubeCordenando.get_atividades().remove(atividade_escolhida)
                print(f"A atividade {atividade_escolhida.get_titulo()} foi excluída com sucesso!")