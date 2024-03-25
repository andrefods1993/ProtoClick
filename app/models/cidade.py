class Cidade:
    def __init__(self, id, descricao, uf_id):
        """
        Inicializa um objeto Cidade com os atributos específicos.

        Args:
            id (int): Identificador único da cidade.
            descricao (str): Descrição da cidade.
            uf_id (int): Identificador da UF referente à cidade.
        """
        self.id = id  # Identificador único da cidade
        self.descricao = descricao  # Descrição da cidade
        self.uf_id = uf_id  # Identificador da UF referente à cidade

    def __str__(self):
        """
        Retorna uma representação em string do objeto Cidade.

        Returns:
            str: Representação em string do objeto Cidade.
        """
        return f"Cidade: {self.descricao}"
