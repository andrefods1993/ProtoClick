from PySide6.QtWidgets import QApplication, QWidget

from app.widgets.toggle_button import ToggleButton
from app.widgets.nav_button import NavButton
from app.widgets.social_button import SocialButton
from app.managers.table_manager import TableManager
from app.managers.empresa_manager import EmpresaManager
from app.managers.combobox_manager import ComboBoxManager
from app.managers.action_manager import *
from app.controllers.user_controller import UserController
from app.controllers.type_controller import TypeController
from app.controllers.warning_controller import WarningController
from app.controllers.client_controller import ClientController
from app.controllers.company_controller import CompanyController
from app.controllers.protoc_controller import ProtocController

from app.integration.genai_integration import formatar_texto_genai

from ui_form import Ui_MainWindow

class Widget(QWidget):
    def __init__(self, parent=None):
        """
        Inicializa o Widget principal da aplicação.

        Args:
            parent (QWidget): Widget pai, se houver. Padrão é None.
        """
        super().__init__(parent)
        # Instancia a classe de interface do usuário
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        # Instancia os elementos da interface
        self.toggle_button = ToggleButton(self.ui)
        self.nav_button = NavButton(self.ui)
        self.social_button = SocialButton(self.ui)


        # Instancia e carrega dados usando gerenciadores
        self.tabela_manager = TableManager(self.ui.tabela_usuarios, self.ui.tabela_clientes,
                                            self.ui.tabela_tiposAtendimento, self.ui.tabela_avisos,
                                            self.ui.tabela_protocolos)
        self.tabela_manager.carregar_usuarios()
        self.tabela_manager.carregar_clientes()
        self.tabela_manager.carregar_tipos_atendimento()
        self.tabela_manager.carregar_avisos()
        self.tabela_manager.carregar_protocolos()


        # Instancia o gerenciador de comboboxes e popula as comboboxes
        self.combo_manager = ComboBoxManager()  # Gerenciador de comboboxes
        self.combo_manager.popular_combo_cidade(self.ui.cb_enderecoClientesCidade)
        self.combo_manager.popular_combo_uf(self.ui.cb_enderecoClientesUF)
        self.combo_manager.popular_combo_cidade(self.ui.cb_empresaCidade)
        self.combo_manager.popular_combo_uf(self.ui.cb_empresaUf)


        # Conecta sinais de botões a funções específicas
        self.ui.btn4_protocolos.clicked.connect(self.on_button_clicked)
         
 
        # Conecta as comboboxes para atualização dinâmica
        conectar_comboboxes(self.ui.cb_enderecoClientesUF,self.ui.cb_enderecoClientesCidade,
                            self.combo_manager)
        conectar_comboboxes(self.ui.cb_empresaUf,self.ui.cb_empresaCidade,
                            self.combo_manager)
        conectar_cliente_solicitante(self.ui.cb_protocolosCliente,self.ui.cb_protocolosSolicitante,
                            self.combo_manager)


        # Instancia os controladores para realizar operações na interface
        self.empresa_manager = EmpresaManager(self.ui)
        self.empresa_manager.carregar_empresa()
        self.user_controller = UserController(self.ui)
        self.type_controller = TypeController(self.ui)
        self.warning_controller = WarningController(self.ui)
        self.client_controller = ClientController(self.ui)
        self.company_controller = CompanyController(self.ui)
        self.protoc_controller = ProtocController(self.ui)


        # Conectando eventos à funcionalidade de pesquisa
        #* ---------- Pesquisa Usuários ---------- *#
        self.ui.btn_pesquisaUsuarios.clicked.connect(self.pesquisar_usuarios)
        self.ui.barLine_pesquisaUsuarios.returnPressed.connect(self.pesquisar_usuarios)
        #* ---------- Pesquisa Clientes ---------- *#
        self.ui.btn_pesquisaClientes.clicked.connect(self.pesquisar_clientes)
        self.ui.barLine_pesquisaClientes.returnPressed.connect(self.pesquisar_clientes)
        #* ---------- Pesquisa Protocolos ---------- *#
        self.ui.btn_pesquisaProtocolos.clicked.connect(self.pesquisar_protocolos)
        self.ui.barLine_pesquisaProtocolos.returnPressed.connect(self.pesquisar_protocolos)
        #* ---------- Pesquisa Tipos de Atendimento ---------- *#
        self.ui.btn_pesquisaTiposAtendimento.clicked.connect(self.pesquisar_tipos_atendimento)
        self.ui.barLine_pesquisaTiposAtendimento.returnPressed.connect(self.pesquisar_tipos_atendimento)
        #* ---------- Pesquisa Avisos ---------- *#
        self.ui.btn_pesquisaAvisos.clicked.connect(self.pesquisar_avisos)
        self.ui.barLine_pesquisaAvisos.returnPressed.connect(self.pesquisar_avisos)


        # Ajusta o tamanho das colunas das tabelas para se adaptar ao conteúdo do texto
        self.ui.tabela_usuarios.resizeColumnsToContents()
        self.ui.tabela_clientes.resizeColumnsToContents()
        self.ui.tabela_protocolos.resizeColumnsToContents()
        self.ui.tabela_tiposAtendimento.resizeColumnsToContents()
        self.ui.tabela_avisos.resizeColumnsToContents()

        self.ui.tabela_protocolos.hideColumn(6)  # Ocultar a coluna de relatório da tabela de protocolos
        # self.ui.tabela_avisos.hideColumn(2)  <--- Caso queira ocultar a coluna de mensagem na tabela Avisos
        self.ui.tabela_avisos.setColumnWidth(2, 300)  # Limitando a coluna de mensagem na tabela Avisos para 300 pixels


        # Conecta o botão btn_protocolosRobot à função de formatação do GPT-3
        self.ui.btn_protocolosRobot.clicked.connect(self.formatar_texto_com_genai)

    def pesquisar_usuarios(self):
        """
        Pesquisa usuários na tabela de acordo com o texto digitado na barra de pesquisa.
        """
        barra_pesquisa = self.ui.barLine_pesquisaUsuarios.text()
        pesquisar_tabela(self.ui.tabela_usuarios, barra_pesquisa)
    
    def pesquisar_clientes(self):
        """
        Pesquisa clientes na tabela de acordo com o texto digitado na barra de pesquisa.
        """
        barra_pesquisa = self.ui.barLine_pesquisaClientes.text()
        pesquisar_tabela(self.ui.tabela_clientes, barra_pesquisa)
    
    def pesquisar_protocolos(self):
        """
        Pesquisa protocolos na tabela de acordo com o texto digitado na barra de pesquisa.
        """
        barra_pesquisa = self.ui.barLine_pesquisaProtocolos.text()
        pesquisar_tabela(self.ui.tabela_protocolos, barra_pesquisa)

    def pesquisar_tipos_atendimento(self):
        """
        Pesquisa tipos de atendimento na tabela de acordo com o texto digitado na barra de pesquisa.
        """
        barra_pesquisa = self.ui.barLine_pesquisaTiposAtendimento.text()
        pesquisar_tabela(self.ui.tabela_tiposAtendimento, barra_pesquisa)

    def pesquisar_avisos(self):
        """
        Pesquisa avisos na tabela de acordo com o texto digitado na barra de pesquisa.
        """
        barra_pesquisa = self.ui.barLine_pesquisaAvisos.text()
        pesquisar_tabela(self.ui.tabela_avisos, barra_pesquisa)
    

    def on_button_clicked(self):
        """
        Método chamado quando um botão é clicado na interface.
        """
        self.combo_manager.popular_combo_atendimento(self.ui.cb_protocolosAtendimento)
        self.combo_manager.popular_combo_consultor(self.ui.cb_protocolosConsultor)
        self.combo_manager.popular_combo_cliente(self.ui.cb_protocolosCliente)
    

    def formatar_texto_com_genai(self):
        # Obtém o texto
        self.data = self.ui.date_protocolosData.date().toString('dd/MM/yyyy')
        self.cliente = self.ui.cb_protocolosCliente.currentText()
        self.tipo_atendimento = self.ui.cb_protocolosAtendimento.currentText()
        self.relatorio = self.ui.ed_protocolosDescricao.toPlainText()

        self.texto_original = (
            f"Data: {self.data}\n"
            f"Cliente: {self.cliente}\n"
            f"Tipo de Atendimento: {self.tipo_atendimento}\n"
            f"Relatório:\n{self.relatorio}\n\n"
        )

        # Chama a função de integração com o Genai para formatar o texto
        texto_formatado = formatar_texto_genai(self.texto_original)

        # Define o texto formatado de volta no QTextEdit
        self.ui.ed_protocolosDescricao.setPlainText(str(texto_formatado))

if __name__ == "__main__":
    # Inicializa a aplicação Qt
    app = QApplication([])
    # Instancia e exibe o widget principal
    widget = Widget()
    widget.show()
    # Executa o loop de eventos da aplicação
    app.exec()
