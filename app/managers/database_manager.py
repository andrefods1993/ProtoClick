import sqlite3

class DatabaseManager:
    def __init__(self, db_path):
        """
        Inicializa o DatabaseManager com o caminho do banco de dados.

        Args:
            db_path (str): Caminho do banco de dados SQLite.
        """
        self.db_path = db_path  # Inicializa o caminho do banco de dados

    def conectar(self):
        """Conecta ao banco de dados especificado."""
        try:
            self.conn = sqlite3.connect(self.db_path)  # Conecta ao banco de dados
            self.cursor = self.conn.cursor()  # Cria um cursor para executar comandos SQL
        except sqlite3.Error as e:
            print("Erro ao conectar ao banco de dados:", e)  # Imprime mensagem de erro em caso de falha na conexão

    def desconectar(self):
        """Desconecta do banco de dados."""
        if self.conn:
            self.conn.close()  # Fecha a conexão com o banco de dados

# Utilização do DatabaseManager com o caminho do banco de dados
db_manager = DatabaseManager("database/protoclick_db.db")  # Instancia o DatabaseManager com o caminho do banco de dados
