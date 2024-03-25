from PySide6.QtWidgets import QMainWindow, QLineEdit
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Carregar a interface do arquivo form.ui
        self.load_ui()

        # Adicionar validador para aceitar somente números
        number_validator = QRegularExpressionValidator("[0-9@#$%]*")
        self.lineEdit.setValidator(number_validator)

    def load_ui(self):
        from PySide6.QtUiTools import QUiLoader
        from PySide6.QtCore import QFile

        # Carregar o arquivo form.ui usando o QUiLoader
        loader = QUiLoader()
        file = QFile("form.ui")
        file.open(QFile.ReadOnly)
        self.widget = loader.load(file, self)
        file.close()

        # Definir a central widget do QMainWindow como o widget carregado
        self.setCentralWidget(self.widget)

        # Encontrar o QLineEdit no widget carregado
        self.lineEdit = self.findChild(QLineEdit, "lineEdit")
