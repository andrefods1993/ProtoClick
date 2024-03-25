class Solicitante:
    def __init__(self, id, nome, cliente_id):
        """
        Inicializa um objeto Solicitante com os atributos específicos.

        Args:
            id (int): Identificador único do cliente.
            nome (str): Nome do solicitante.
            cliente_id (int): Id do cliente vinculado
        """
        self.id = id  # Identificador único do solicitante
        self.nome = nome  # Nome do solicitante
        self.cliente_id = cliente_id  # Id do cliente vinculado

    def __str__(self):
        """
        Retorna uma representação em string do objeto Solicitante.

        Returns:
            str: Representação em string do objeto Solicitante.
        """
        return f"Solicitante: ({self.id}) {self.nome}"
