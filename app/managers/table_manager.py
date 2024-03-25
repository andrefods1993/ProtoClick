from PySide6.QtWidgets import QTableWidgetItem
from app.managers.data_manager import DataManager
from PySide6.QtCore import Qt

class TableManager:
    def __init__(self, tabela_usuarios=None, tabela_clientes=None,
                 tabela_tiposAtendimento=None, tabela_avisos=None, tabela_protocolos=None):
        """
        Inicializa o gerenciador de tabelas com as tabelas fornecidas como argumento.

        Args:
            tabela_usuarios (QTableWidget): Tabela de usuários.
            tabela_clientes (QTableWidget): Tabela de clientes.
            tabela_tiposAtendimento (QTableWidget): Tabela de tipos de atendimento.
            tabela_avisos (QTableWidget): Tabela de avisos.
        """
        # Instancia as tabelas fornecidas como argumento
        self.tabela_usuarios = tabela_usuarios
        self.tabela_clientes = tabela_clientes
        self.tabela_tiposAtendimento = tabela_tiposAtendimento
        self.tabela_avisos = tabela_avisos
        self.tabela_protocolos = tabela_protocolos

        self.data = DataManager()  # Instancia o gerenciador de dados

    def carregar_usuarios(self):
        """
        Carrega os usuários na tabela de usuários.
        """
        # Limpa o conteúdo da tabela antes de carregar os usuários novamente
        self.tabela_usuarios.clearContents()
        self.tabela_usuarios.setRowCount(0)

        # Busca todos os usuários do banco de dados utilizando o DataManager
        usuarios = self.data.buscar_usuarios()

        # Define o número de linhas na tabela com base na quantidade de usuários encontrados
        self.tabela_usuarios.setRowCount(len(usuarios))

        # Preenche a tabela com os dados dos usuários
        for row, usuario in enumerate(usuarios):
            # Insere os dados do usuário em cada célula da tabela
            id_item = QTableWidgetItem()
            id_item.setData(Qt.DisplayRole, usuario.id)
            self.tabela_usuarios.setItem(row, 0, id_item)
            self.tabela_usuarios.setItem(row, 1, QTableWidgetItem(usuario.nome))
            self.tabela_usuarios.setItem(row, 2, QTableWidgetItem(str(usuario.contato)))
            self.tabela_usuarios.setItem(row, 3, QTableWidgetItem(usuario.email))
            self.tabela_usuarios.setItem(row, 4, QTableWidgetItem(usuario.funcao))
            self.tabela_usuarios.setItem(row, 5, QTableWidgetItem(usuario.desativado))


    def carregar_clientes(self):
        """
        Carrega os clientes na tabela de clientes.
        """
        # Limpa o conteúdo da tabela antes de carregar os clientes novamente
        self.tabela_clientes.clearContents()
        self.tabela_clientes.setRowCount(0)

        # Busca todos os clientes do banco de dados utilizando o DataManager
        clientes = self.data.buscar_clientes()

        # Define o número de linhas na tabela com base na quantidade de clientes encontrados
        self.tabela_clientes.setRowCount(len(clientes))

        # Preenche a tabela com os dados dos clientes
        for row, cliente in enumerate(clientes):
            # Insere os dados do cliente em cada célula da tabela
            id_item = QTableWidgetItem()
            id_item.setData(Qt.DisplayRole, cliente.id)
            self.tabela_clientes.setItem(row, 0, id_item)
            self.tabela_clientes.setItem(row, 1, QTableWidgetItem(cliente.razao_social))
            self.tabela_clientes.setItem(row, 2, QTableWidgetItem(str(cliente.cpf_cnpj)))
            self.tabela_clientes.setItem(row, 3, QTableWidgetItem(cliente.natureza_social))
            self.tabela_clientes.setItem(row, 4, QTableWidgetItem(str(cliente.contato)))
            self.tabela_clientes.setItem(row, 5, QTableWidgetItem(cliente.email))
            self.tabela_clientes.setItem(row, 6, QTableWidgetItem(cliente.solicitante))
            self.tabela_clientes.setItem(row, 7, QTableWidgetItem(str(cliente.cep)))
            self.tabela_clientes.setItem(row, 8, QTableWidgetItem(cliente.logradouro))
            self.tabela_clientes.setItem(row, 9, QTableWidgetItem(str(cliente.numero)))
            self.tabela_clientes.setItem(row, 10, QTableWidgetItem(cliente.bairro))
            self.tabela_clientes.setItem(row, 11, QTableWidgetItem(cliente.cidade))
            self.tabela_clientes.setItem(row, 12, QTableWidgetItem(cliente.uf))
            self.tabela_clientes.setItem(row, 13, QTableWidgetItem(cliente.referencia))
            self.tabela_clientes.setItem(row, 14, QTableWidgetItem(cliente.desativado))


    def carregar_tipos_atendimento(self):
        """
        Carrega os tipos de atendimento na tabela de tipos de atendimento.
        """
        # Limpa o conteúdo da tabela antes de carregar os tipos de atendimento novamente
        self.tabela_tiposAtendimento.clearContents()
        self.tabela_tiposAtendimento.setRowCount(0)

        # Busca todos os tipos de atendimento do banco de dados utilizando o DataManager
        tipos_atendimento = self.data.buscar_tipos_atendimento()

        # Define o número de linhas na tabela com base na quantidade de tipos de atendimento encontrados
        self.tabela_tiposAtendimento.setRowCount(len(tipos_atendimento))

        # Preenche a tabela com os dados dos tipos de atendimento
        for row, tipo_atendimento in enumerate(tipos_atendimento):
            # Insere os dados do tipo de atendimento em cada célula da tabela
            id_item = QTableWidgetItem()
            id_item.setData(Qt.DisplayRole, tipo_atendimento.id)
            self.tabela_tiposAtendimento.setItem(row, 0, id_item)
            self.tabela_tiposAtendimento.setItem(row, 1, QTableWidgetItem(tipo_atendimento.descricao))
            self.tabela_tiposAtendimento.setItem(row, 2, QTableWidgetItem(tipo_atendimento.desativado))


    def carregar_avisos(self):
        """
        Carrega os avisos na tabela de avisos.
        """
        # Limpa o conteúdo da tabela antes de carregar os avisos novamente
        self.tabela_avisos.clearContents()

        # Busca todos os avisos do banco de dados utilizando o DataManager
        avisos = self.data.buscar_avisos()

        # Define o número de linhas na tabela com base na quantidade de avisos encontrados
        self.tabela_avisos.setRowCount(len(avisos))

        # Preenche a tabela com os dados dos avisos
        for row, aviso in enumerate(avisos):
            # Insere os dados do aviso em cada célula da tabela
            id_item = QTableWidgetItem()
            id_item.setData(Qt.DisplayRole, aviso.id)
            self.tabela_avisos.setItem(row, 0, id_item)
            self.tabela_avisos.setItem(row, 1, QTableWidgetItem(aviso.descricao))
            self.tabela_avisos.setItem(row, 2, QTableWidgetItem(aviso.mensagem))
            self.tabela_avisos.setItem(row, 3, QTableWidgetItem(aviso.desativado))


    def carregar_protocolos(self):
        """
        Carrega os protocolos na tabela de protocolos.

        Este método limpa o conteúdo da tabela de protocolos e carrega os protocolos do banco de dados.
        Os dados dos protocolos são inseridos nas células da tabela para exibição na interface.
        """
        # Limpa o conteúdo da tabela antes de carregar os protocolos novamente
        self.tabela_protocolos.clearContents()
        self.tabela_protocolos.setRowCount(0)

        # Busca todos os protocolos do banco de dados utilizando o DataManager
        protocolos = self.data.buscar_protocolos()

        # Define o número de linhas na tabela com base na quantidade de protocolos encontrados
        self.tabela_protocolos.setRowCount(len(protocolos))

        # Preenche a tabela com os dados dos protocolos
        for row, protocolo in enumerate(protocolos):
            # Insere os dados do protocolo em cada célula da tabela
            id_item = QTableWidgetItem()
            id_item.setData(Qt.DisplayRole, protocolo.id)
            self.tabela_protocolos.setItem(row, 0, id_item)
            self.tabela_protocolos.setItem(row, 1, QTableWidgetItem(str(protocolo.data)))
            self.tabela_protocolos.setItem(row, 2, QTableWidgetItem(protocolo.cliente))
            self.tabela_protocolos.setItem(row, 3, QTableWidgetItem(protocolo.solicitante))
            self.tabela_protocolos.setItem(row, 4, QTableWidgetItem(protocolo.consultor))
            self.tabela_protocolos.setItem(row, 5, QTableWidgetItem(protocolo.tipo_atendimento))
            self.tabela_protocolos.setItem(row, 6, QTableWidgetItem(protocolo.relatorio))
            self.tabela_protocolos.setItem(row, 7, QTableWidgetItem(str(protocolo.hora_inicio)))
            self.tabela_protocolos.setItem(row, 8, QTableWidgetItem(str(protocolo.hora_termino)))
            self.tabela_protocolos.setItem(row, 9, QTableWidgetItem(protocolo.cancelado))
