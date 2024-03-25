class Aviso:
    def __init__(self, id, descricao, mensagem, desativado):
        """
        Inicializa um objeto Aviso com os atributos específicos.

        Args:
            id (int): Identificador único do aviso.
            descricao (str): Descrição do aviso.
            desativado (bool): Indica se o aviso está desativado (True) ou não (False).
        """
        self.id = id  # Identificador único do aviso
        self.descricao = descricao  # Descrição do aviso
        self.mensagem = mensagem  # Mensagem do aviso
        self.desativado = desativado  # Indica se o aviso está desativado ou não

    def __str__(self):
        """
        Retorna uma representação em string do objeto Aviso.

        Returns:
            str: Representação em string do objeto Aviso.
        """
        return f"Aviso: {self.descricao}"
