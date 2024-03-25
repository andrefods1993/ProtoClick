from PySide6.QtCore import QThread
from docx2pdf import convert
from app.widgets.progressdialog import ProgressDialog

class ConverterPDFThread(QThread):


    def __init__(self, input_path, output_path):
        """
        Inicializa a classe ConverterPDFThread.

        :param input_path: Caminho do arquivo de entrada (DOCX).
        :param output_path: Caminho de saída para o arquivo convertido (PDF).
        """
        super().__init__()  # Chama o inicializador da classe pai (QThread)
        self.input_path = input_path  # Define o caminho do arquivo de entrada
        self.output_path = output_path  # Define o caminho do arquivo de saída
        self.progress_dialog = ProgressDialog()  # Instancia um ProgressDialog para exibir o progresso

    def run(self):
        """
        Método que executa a conversão de DOCX para PDF na thread.

        Emite sinais de progresso conforme a conversão é realizada e trata exceções se houver erros.
        """
        try:
            # Realiza a conversão de DOCX para PDF
            convert(self.input_path, self.output_path)

        except Exception as e:
            # Em caso de erro, imprime a mensagem de erro e emite o sinal de progresso 0%
            print(f"Erro ao converter o arquivo: {e}")

    def start(self):
        """
        Método para iniciar a thread de conversão.
        """
        super().start()  # Inicia a execução da thread

    def terminate(self):
        """
        Método para terminar a thread de conversão.
        """
        super().terminate()  # Encerra a execução da thread
