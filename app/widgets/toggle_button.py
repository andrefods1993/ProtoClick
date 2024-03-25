from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize, QPropertyAnimation, QEasingCurve

class ToggleButton:
    def __init__(self, ui):
        """" Inicializa o ToggleButton com a interface de usuário fornecida. """
        self.ui = ui  # Armazena a interface de usuário como atributo

        # Define os ícones e imagens para o botão e o logo
        self.icon_collapsed = QIcon("assets/icons/arrow-right.svg")
        self.icon_expanded = QIcon("assets/icons/arrow-left.svg")
        self.logo_collapsed = QPixmap("assets/icons/logo_p.png")
        self.logo_expanded = QPixmap("assets/icons/logo_protoclick.png")
        self.btn_collapsed = 35
        self.btn_expanded = 200

        # Configura os ícones e imagens iniciais
        self.ui.btn_toggleButton.setIcon(self.icon_expanded)
        self.ui.logo.setPixmap(self.logo_expanded)
        self.ui.nav.setMaximumWidth(200)
        self.ui.btn1_home.setMaximumWidth(self.btn_expanded)
        self.ui.btn2_usuarios.setMaximumWidth(self.btn_expanded)
        self.ui.btn3_clientes.setMaximumWidth(self.btn_expanded)
        self.ui.btn4_protocolos.setMaximumWidth(self.btn_expanded)
        self.ui.btn1_empresa.setMaximumWidth(self.btn_expanded)
        self.ui.btn2_tipoAtendimento.setMaximumWidth(self.btn_expanded)
        self.ui.btn3_avisos.setMaximumWidth(self.btn_expanded)
        self.ui.btn4_sobre.setMaximumWidth(self.btn_expanded)

        # Inicializa as animações para o ícone do botão e a largura do menu
        self.icon_animation = QPropertyAnimation(self.ui.btn_toggleButton, b'iconSize')
        self.icon_animation.setDuration(400)  # Velocidade da animação
        self.icon_animation.setEasingCurve(QEasingCurve.InOutQuad)

        self.menu_animation = QPropertyAnimation(self.ui.nav, b"maximumWidth")
        self.menu_animation.setDuration(400)  # Velocidade da animação
        self.menu_animation.setEasingCurve(QEasingCurve.InOutQuart)

        # Conecta o sinal 'clicked' do botão à função toggle_menu
        self.ui.btn_toggleButton.clicked.connect(self.toggle_menu)

    def toggle_menu(self):
        """Alterna entre o menu expandido e recolhido ao clicar no botão."""
        # Obtém a largura atual do menu
        width = self.ui.nav.maximumWidth()

        # Define a nova largura, ícone e imagem do logo com base na largura atual
        new_width, icon, logo, btn = (
            200,
            self.icon_expanded,
            self.logo_expanded,
            self.btn_expanded,
        ) if width == 80 else (
            80,
            self.icon_collapsed,
            self.logo_collapsed,
            self.btn_collapsed,
        )

        # Altera o ícone do botão e a imagem do logo
        self.ui.btn_toggleButton.setIcon(icon)
        self.ui.logo.setPixmap(logo)
        self.ui.btn1_home.setMaximumWidth(btn)
        self.ui.btn2_usuarios.setMaximumWidth(btn)
        self.ui.btn3_clientes.setMaximumWidth(btn)
        self.ui.btn4_protocolos.setMaximumWidth(btn)
        self.ui.btn1_empresa.setMaximumWidth(btn)
        self.ui.btn2_tipoAtendimento.setMaximumWidth(btn)
        self.ui.btn3_avisos.setMaximumWidth(btn)
        self.ui.btn4_sobre.setMaximumWidth(btn)

        # Configura os valores de início e fim para a animação do ícone do botão
        self.icon_animation.setStartValue(QSize(10, 10))
        self.icon_animation.setEndValue(QSize(20, 20))
        self.icon_animation.start()

        # Configura os valores de início e fim para a animação da largura do menu
        self.menu_animation.setStartValue(width)
        self.menu_animation.setEndValue(new_width)
        self.menu_animation.start()
