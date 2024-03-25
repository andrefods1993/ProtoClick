class NavButton:
    def __init__(self, ui):
        """Inicializa o NavButton com a interface de usuário fornecida."""
        self.ui = ui  # Armazena a interface de usuário como atributo

        # Conecta os sinais 'clicked' dos botões às respectivas funções lambda
        self.ui.btn1_home.clicked.connect(lambda: self.ui.section.setCurrentWidget(self.ui.s1_home))
        self.ui.btn2_usuarios.clicked.connect(lambda: self.ui.section.setCurrentWidget(self.ui.s2_usuarios))
        self.ui.btn3_clientes.clicked.connect(lambda: self.ui.section.setCurrentWidget(self.ui.s3_clientes))
        self.ui.btn4_protocolos.clicked.connect(lambda: self.ui.section.setCurrentWidget(self.ui.s4_protocolos))
        self.ui.btn1_empresa.clicked.connect(lambda: self.ui.section.setCurrentWidget(self.ui.s5_empresas))
        self.ui.btn2_tipoAtendimento.clicked.connect(lambda: self.ui.section.setCurrentWidget(self.ui.s6_tipos_atendimento))
        self.ui.btn3_avisos.clicked.connect(lambda: self.ui.section.setCurrentWidget(self.ui.s7_avisos))
        self.ui.btn4_sobre.clicked.connect(lambda: self.ui.section.setCurrentWidget(self.ui.s8_sobre))
