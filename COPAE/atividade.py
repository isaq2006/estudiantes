from datetime import datetime
from datetime import datetime

class Atividade:
    def __init__(self, titulo="", descricao="", data_vencimento="", tipo_arquivo="", respostas=None):
        self.__titulo = titulo
        self.__descricao = descricao
        self.__data_criacao = datetime.now()
        self.__data_vencimento = data_vencimento
        self.__tipo_arquivo = tipo_arquivo
        self.__respostas = respostas

    def concluir(self,id_autor):
        from arquivo import Arquivo
        """
        Conclui a atividade.
        """
        if self.__data_vencimento  < datetime.now():
            print("A data de vencimento desta atividade já foi ultrapassada.")
        else:
            print("fazer upload do arquivo da atividade")
            arquivoAtividade = Arquivo()
            arquivoAtividade.editar_arquivo(id_autor)
            self.__respostas.append(arquivoAtividade)
            print("A atividade foi concluída com sucesso!")

    def visualizar(self):
        """
        Exibe detalhes da atividade.
        """
        print("Atividade:")
        print(f"\nTítulo: {self.__titulo}")
        print(f"\nDescrição: {self.__descricao}")
        print(f"\nData de Criação: {self.__data_criacao}")
        print(f"\nData de Vencimento: {self.__data_vencimento}")
        print(f"\nTipo de Arquivo: {self.__tipo_arquivo}")
        if self.__arquivo:
            print(f"\nArquivo: {self.__arquivo.get_titulo()}")
        else:
            print("\nArquivo: Nenhum arquivo enviado")
            
    def visualisar_respostas(self):
        for i, resposta in enumerate(self.respostas, 1):
            print(i)
            resposta.visualizar()

    # Métodos getters
    def get_titulo(self):
        return self.__titulo

    def get_descricao(self):
        return self.__descricao

    def get_data_criacao(self):
        return self.__data_criacao

    def get_data_vencimento(self):
        return self.__data_vencimento

    def get_tipo_arquivo(self):
        return self.__tipo_arquivo

    def get_respostas(self):
        return self.get_respostas

    # Métodos setters
    def set_titulo(self, titulo: str):
        self.__titulo = titulo

    def set_descricao(self, descricao: str):
        self.__descricao = descricao

    def set_data_criacao(self, data_criacao: float):
        self.__data_criacao = data_criacao

    def set_data_vencimento(self, data_vencimento: float):
        self.__data_vencimento = data_vencimento

    def set_tipo_arquivo(self, tipo_arquivo: str):
        self.__tipo_arquivo = tipo_arquivo

    def set_arquivo(self, arquivo):
        self.__arquivo = arquivo
