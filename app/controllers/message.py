from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QIcon

class Message:
    def __init__(self):
        # Inicializa a caixa de mensagem
        self.msg_box = QMessageBox()
        # Define o ícone para a caixa de mensagem
        self.icon = QIcon('assets/icons/logo_p.png')

    def mensagem_aviso(self, msg_title, msg):
        """
        Exibe uma mensagem de aviso.

        Args:
            msg_title (str): Título da mensagem.
            msg (str): Conteúdo da mensagem.
        """
        self.msg_box.setIcon(QMessageBox.Icon.Warning)
        self.msg_box.setWindowTitle(msg_title)
        self.msg_box.setText(msg)
        self.msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.msg_box.setWindowIcon(self.icon)
        self.msg_box.setStyleSheet(style_sheet)  # Aplica a folha de estilo definida
        self.msg_box.exec()


    def mensagem_informacao(self, msg_title, msg):
        """
        Exibe uma mensagem informativa.

        Args:
            msg_title (str): Título da mensagem.
            msg (str): Conteúdo da mensagem.
        """
        self.msg_box.setIcon(QMessageBox.Icon.Information)
        self.msg_box.setWindowTitle(msg_title)
        self.msg_box.setText(msg)
        self.msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        self.msg_box.setWindowIcon(self.icon)
        self.msg_box.setStyleSheet(style_sheet)  # Aplica a folha de estilo definida
        resultado = self.msg_box.exec()

        if resultado == QMessageBox.StandardButton.Ok:
            return "Ok"

    def mensagem_confirmacao(self, msg_title, msg):
        """
        Exibe uma mensagem de confirmação com opção "Sim" ou "Não".

        Args:
            msg_title (str): Título da mensagem.
            msg (str): Conteúdo da mensagem.

        Returns:
            str: Retorna "Yes" se a opção "Sim" for escolhida, "No" se a opção "Não" for escolhida.
        """
        self.msg_box.setIcon(QMessageBox.Icon.Warning)
        self.msg_box.setWindowTitle(msg_title)
        self.msg_box.setText(msg)
        self.msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        self.msg_box.button(QMessageBox.StandardButton.Yes).setText('Sim')  # Altera o texto do botão "Yes" para "Sim"
        self.msg_box.button(QMessageBox.StandardButton.No).setText('Não')  # Altera o texto do botão "No" para "Não"
        self.msg_box.setWindowIcon(self.icon)
        self.msg_box.setStyleSheet(style_sheet)  # Aplica a folha de estilo definida
        
        # Encontre o botão 'Yes' e aplique a folha de estilo
        no_button = self.msg_box.button(QMessageBox.StandardButton.No)
        if no_button:
            no_button.setStyleSheet(style_sheet_no)

        resultado = self.msg_box.exec()

        if resultado == QMessageBox.StandardButton.Yes:
            return "Yes"
        else:
            return "No"

# Folha de estilo para a caixa de mensagem
style_sheet = """
    QMessageBox {
        background-color: #FCFCFC;
        border: 2px solid #00718F;
        border-bottom-left-radius: 7px;
        border-bottom-right-radius: 7px;
        color: #171C25;
        font-size: 16px;
    }

    QMessageBox QLabel {
        color: #171C25;
        font-size: 16px;
    }

    QMessageBox QPushButton {
        padding: 5px 10px;
        background-color: #00718F;
        color: #FFF;
        border: 1px solid #00718F;
        border-radius: 5px;
        font-size: 16px;
    }

    QMessageBox QPushButton:hover {
        background-color: #00546B;
    }

    QMessageBox QPushButton:pressed {
        background-color: #003D4A;
    }
"""
style_sheet_no = """
    QMessageBox QPushButton {
        padding: 5px 10px;
        background-color: #8f1e00;
        color: #FFF;
        border: 1px solid #8f1e00;
        border-radius: 5px;
        font-size: 16px;
    }

    QMessageBox QPushButton:hover {
        background-color: #6b1700;
    }

    QMessageBox QPushButton:pressed {
        background-color: #4a0d00;
    }
"""