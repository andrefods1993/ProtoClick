from PySide6.QtWidgets import QProgressDialog
from PySide6.QtCore import QTimer, Qt

class ProgressDialog:
    def __init__(self):
        """
        Inicializa a classe ProgressDialog.
        """
        self.steps = 0  # Inicializa o contador de passos
        self.pd = QProgressDialog("Salvando... Aguarde um momento, por favor.", "", 0, 100)  # Cria o diálogo de progresso
        self.pd.setWindowTitle('Salvando em PDF')  # Define o título do diálogo
        self.pd.setCancelButton(None)
        # Configura as flags do diálogo para janela personalizada e manter no topo
        self.pd.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.CustomizeWindowHint | Qt.WindowType.WindowStaysOnTopHint | Qt.WindowType.WindowTitleHint)
        self.t = QTimer()  # Cria um QTimer para atualizar o progresso
        self.t.timeout.connect(self.perform)  # Conecta o sinal timeout do QTimer ao método perform
        self.t.start(35)  # Inicia o QTimer com um intervalo de 35 milissegundos (atualização do progresso)
        # Aplica o estilo ao diálogo de progresso
        self.apply_style()

    def apply_style(self):
        """
        Aplica um estilo ao QProgressDialog.
        """
        style = """
            QProgressDialog {
                background-color: #FCFCFC;
                border: 2px solid #00718F;
                border-bottom-left-radius: 7px;
                border-bottom-right-radius: 7px;
                color: #171C25;
                font-size: 14px;
            }
            QProgressDialog QLabel {
                color: #171C25;
                font-size: 14px;
            }
        """
        self.pd.setStyleSheet(style)

    def perform(self):
        """
        Método para realizar a operação simulada e atualizar o progresso.
        """
        self.pd.setValue(self.steps)  # Define o valor de progresso no diálogo
        # Simula uma operação longa (substitua este código pela sua operação real)
        # Exemplo: for i in range(1000000): pass
        self.steps += 1  # Incrementa o contador de passos
        if self.steps > self.pd.maximum():  # Verifica se o progresso atingiu o máximo
            self.t.stop()  # Para o QTimer
            self.pd.close()  # Fecha o diálogo após a conclusão da operação

    def cancel(self):
        """
        Método para cancelar a operação e fechar o diálogo.
        """
        self.t.stop()  # Para o QTimer
        self.pd.close()  # Fecha o diálogo
        # Adicione aqui a lógica para limpar ou cancelar sua operação