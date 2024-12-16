# Importa o módulo datetime para gerenciar as datas de criação e vencimento da atividade
from datetime import datetime

# Definição da classe Atividade
class Atividade:
    def __init__(self, titulo="", descricao="", data_vencimento="", tipo_arquivo="", respostas=None):
        # Inicializa os atributos da atividade com valores padrão ou recebidos no construtor
        self.__titulo = titulo  # Título da atividade
        self.__descricao = descricao  # Descrição da atividade
        self.__data_criacao = datetime.now()  # Define a data de criação como a data atual
        self.__data_vencimento = data_vencimento  # Data de vencimento da atividade
        self.__tipo_arquivo = tipo_arquivo  # Tipo de arquivo exigido para a atividade
        self.__respostas = []  # Lista de respostas da atividade, inicializada como lista vazia

    # Método para concluir a atividade, verificando se a data de vencimento foi ultrapassada
    def concluir(self, id_autor):
        from arquivo import Arquivo
        # Verifica se a data de vencimento foi ultrapassada
        if self.__data_vencimento < datetime.now():
            print("A data de vencimento desta atividade já foi ultrapassada.")
        else:
            print("Faça o upload do arquivo da atividade.")
            arquivoAtividade = Arquivo()  # Cria uma instância de Arquivo
            arquivoAtividade.enviar_arquivo(id_autor)  # Edita o arquivo usando o ID do autor
            self.__respostas.append(arquivoAtividade)  # Adiciona o arquivo à lista de respostas
            print("A atividade foi concluída com sucesso!")

    # Método para exibir os detalhes da atividade
    def visualizar(self):
        """
        Exibe detalhes da atividade.
        """
        print(f"Título: {self.__titulo}")
        print(f"Descrição: {self.__descricao}")
        print(f"Data de Criação: {self.__data_criacao}")
        print(f"Data de Vencimento: {self.__data_vencimento}")
        print(f"Tipo de Arquivo: {self.__tipo_arquivo}\n")

    # Método para visualizar todas as respostas da atividade
    def visualisar_respostas(self):
        if not self.__respostas:
            print("Nenhuma resposta enviada at[e o momento]")
        else:
            for i, resposta in enumerate(self.__respostas, 1):
                print(f"\nResposta {i}:")
                resposta.visualizar()  # Chama o método visualizar de cada resposta (objeto Arquivo)

    # Métodos getters para acessar os atributos privados
    def get_titulo(self):
        return self.__titulo  # Retorna o título da atividade

    def get_descricao(self):
        return self.__descricao  # Retorna a descrição da atividade

    def get_data_criacao(self):
        return self.__data_criacao  # Retorna a data de criação da atividade

    def get_data_vencimento(self):
        return self.__data_vencimento  # Retorna a data de vencimento da atividade

    def get_tipo_arquivo(self):
        return self.__tipo_arquivo  # Retorna o tipo de arquivo exigido pela atividade

    def get_respostas(self):
        return self.__respostas  # Retorna a lista de respostas da atividade

    # Métodos setters para modificar os atributos privados
    def set_respostas(self, resposta):  # Recebe uma lista de respostas
        for respostax in self.__respostas:
            if respostax.get_id_autor() == resposta.get_id_autor():
                self.__respostas.remove(respostax)
            else:
                pass
        self.__respostas.append(resposta)  # Adiciona a resposta à lista de respostas da atividade
    def set_titulo(self, titulo: str):
        self.__titulo = titulo  # Define um novo título para a atividade

    def set_descricao(self, descricao: str):
        self.__descricao = descricao  # Define uma nova descrição para a atividade

    def set_data_criacao(self, data_criacao: datetime):
        self.__data_criacao = data_criacao  # Define uma nova data de criação para a atividade

    def set_data_vencimento(self, data_vencimento: datetime):
        self.__data_vencimento = data_vencimento  # Define uma nova data de vencimento para a atividade

    def set_tipo_arquivo(self, tipo_arquivo: str):
        self.__tipo_arquivo = tipo_arquivo  # Define um novo tipo de arquivo para a atividade

    def set_arquivo(self, arquivo):
        self.__arquivo = arquivo  # Define um arquivo específico para a atividade
