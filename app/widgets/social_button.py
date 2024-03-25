from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import QUrl

class SocialButton:
    def __init__(self, ui):
        """Inicializa o SocialButton com a interface de usuário fornecida."""
        self.ui = ui  # Armazena a interface de usuário como atributo

        # Define os URLs para cada botão social
        self.whatsapp = QUrl("https://wa.me/5573981547597?text=Ol%C3%A1%21++Gostaria+de+conversar+sobre+o+ProtoClick.+%F0%9F%98%8A%F0%9F%9A%80")
        self.instagram = QUrl("https://www.instagram.com/andrefilipeos/")
        self.linkedin = QUrl("https://www.linkedin.com/in/andrefilipeods")
        self.github = QUrl("https://github.com/andrefods1993")
        self.email = QUrl("mailto:odsandrefilipe@gmail.com?subject=ProtoClick&body=Ol%C3%A1!+Gostaria+de+conversar+sobre+o+ProtoClick.+%E2%98%BA%F0%9F%9A%80")

        # Conecta os sinais 'clicked' dos botões aos métodos correspondentes
        self.ui.btn1_whatsApp.clicked.connect(self.open_whatsapp)
        self.ui.btn2_instagram.clicked.connect(self.open_instagram)
        self.ui.btn3_linkedin.clicked.connect(self.open_linkedin)
        self.ui.btn4_github.clicked.connect(self.open_github)
        self.ui.btn5_email.clicked.connect(self.open_email)

    def open_whatsapp(self):
        """Abre o link do WhatsApp no navegador padrão."""
        QDesktopServices.openUrl(self.whatsapp)

    def open_instagram(self):
        """Abre o link do Instagram no navegador padrão."""
        QDesktopServices.openUrl(self.instagram)

    def open_linkedin(self):
        """Abre o link do LinkedIn no navegador padrão."""
        QDesktopServices.openUrl(self.linkedin)

    def open_github(self):
        """Abre o link do GitHub no navegador padrão."""
        QDesktopServices.openUrl(self.github)

    def open_email(self):
        """Abre o cliente de e-mail padrão com um novo e-mail pré-preenchido."""
        QDesktopServices.openUrl(self.email)
