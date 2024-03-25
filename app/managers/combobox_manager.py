from PySide6.QtWidgets import QComboBox
from app.managers.data_manager import DataManager

# Definição da classe ComboBoxManager
class ComboBoxManager:
    def __init__(self):
        self.data_manager = DataManager()  # Inicialização do DataManager na instância de ComboBoxManager

    # Método para popular o combo_box de cidades
    def popular_combo_cidade(self, combo_box: QComboBox):
        """
        Popula o ComboBox de cidades com dados do DataManager.

        Args:
            combo_box (QComboBox): ComboBox de cidades a ser populado.
        """
        combo_box.clear()  # Limpa o conteúdo do combo_box
        cidades = self.data_manager.buscar_cidades()  # Obtém a lista de cidades do DataManager
        for cidade in cidades:
            combo_box.addItem(cidade.descricao, userData=cidade.id)  # Adiciona itens ao combo_box


    # Método para popular o combo_box de unidades federativas (UF)
    def popular_combo_uf(self, combo_box: QComboBox):
        """
        Popula o ComboBox de UFs com dados do DataManager.

        Args:
            combo_box (QComboBox): ComboBox de UFs a ser populado.
        """
        combo_box.clear()  # Limpa o conteúdo do combo_box
        ufs = self.data_manager.buscar_uf()  # Obtém a lista de UFs do DataManager
        for uf in ufs:
            combo_box.addItem(uf.uf, userData=uf.id)  # Adiciona itens ao combo_box


    # Método para atualizar as cidades com base na UF selecionada
    def atualizar_cidade(self, combo_uf: QComboBox, combo_cidade: QComboBox):
        """
        Atualiza o ComboBox de cidades com base na UF selecionada.

        Args:
            combo_uf (QComboBox): ComboBox de UFs com a UF selecionada.
            combo_cidade (QComboBox): ComboBox de cidades a ser atualizado.
        """
        uf_id = combo_uf.currentData()  # Obtém o ID da UF selecionada no combo_uf
        cidades = self.data_manager.buscar_cidades_por_uf(uf_id)  # Obtém as cidades da UF selecionada
        combo_cidade.clear()  # Limpa o conteúdo do combo_cidade
        for cidade in cidades:
            combo_cidade.addItem(cidade.descricao, userData=cidade.id)  # Adiciona itens ao combo_cidade


    def popular_combo_atendimento(self, combo_box: QComboBox):
        """
        Popula o ComboBox de atendimento com dados do DataManager.

        Args:
            combo_box (QComboBox): ComboBox de atendimento a ser populado.
        """
        combo_box.clear()  # Limpa o conteúdo do combo_box
        atendimentos = self.data_manager.buscar_tipos_atendimento()  # Obtém a lista de atendimentos do DataManager
        for atendimento in atendimentos:
            combo_box.addItem(atendimento.descricao, userData=atendimento.id)  # Adiciona itens ao combo_box
        combo_box.setCurrentIndex(-1)


    def popular_combo_consultor(self, combo_box: QComboBox):
        """
        Popula o ComboBox de consultor com dados do DataManager.

        Args:
            combo_box (QComboBox): ComboBox de consultor a ser populado.
        """
        combo_box.clear()  # Limpa o conteúdo do combo_box
        consultores = self.data_manager.buscar_usuarios()  # Obtém a lista de consultores do DataManager
        for consultor in consultores:
            combo_box.addItem(consultor.nome, userData=consultor.id)  # Adiciona itens ao combo_box
        combo_box.setCurrentIndex(-1)


    def popular_combo_cliente(self, combo_box: QComboBox):
        """
        Popula o ComboBox de cliente com dados do DataManager.

        Args:
            combo_box (QComboBox): ComboBox de cliente a ser populado.
        """
        combo_box.clear()  # Limpa o conteúdo do combo_box
        clientes = self.data_manager.buscar_clientes()  # Obtém a lista de clientes do DataManager
        for cliente in clientes:
            combo_box.addItem(cliente.razao_social, userData=cliente.id)  # Adiciona itens ao combo_box
        combo_box.setCurrentIndex(-1)


    def popular_combo_solicitante(self, combo_box: QComboBox):
        """
        Popula o ComboBox de solicitante com dados do DataManager.

        Args:
            combo_box (QComboBox): ComboBox de solicitante a ser populado.
        """
        combo_box.clear()  # Limpa o conteúdo do combo_box
        solicitantes = self.data_manager.buscar_clientes()  # Obtém a lista de clientes do DataManager
        for solicitante in solicitantes:
            combo_box.addItem(solicitante.solicitante, userData=solicitante.id)  # Adiciona itens ao combo_box


    def atualizar_solicitante(self, combo_cliente: QComboBox, combo_solicitante: QComboBox):
        """
        Atualiza o ComboBox do solicitante com base no cliente selecionado.

        Args:
            combo_cliente (QComboBox): ComboBox de clientes com o cliente selecionado.
            combo_solicitante (QComboBox): ComboBox de solicitante a ser atualizado.
        """
        cliente_id = combo_cliente.currentData()  # Obtém o ID do cliente selecionado no combo_ciente
        solicitantes = self.data_manager.buscar_solicitante_por_cliente(cliente_id)  # Obtém o solicitante do cliente selecionado
        combo_solicitante.clear()  # Limpa o conteúdo do combo_solicitante
        for solicitante in solicitantes:
            combo_solicitante.addItem(solicitante.nome, userData=solicitante.id)  # Adiciona itens ao combo_solicitante

