class UF:
    def __init__(self, id, descricao, uf):
        """
        Inicializa um objeto UF com os atributos específicos.

        Args:
            id (int): Identificador único da UF.
            descricao (str): Descrição da UF.
            uf (str): Abreviação da UF.
        """
        self.id = id  # Identificador único da UF
        self.descricao = descricao  # Descrição da UF
        self.uf = uf  # Abreviação da UF

    def __str__(self):
        """
        Retorna uma representação em string do objeto UF.

        Returns:
            str: Representação em string do objeto UF.
        """
        return f"UF: {self.descricao}"
