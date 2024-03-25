class TipoAtendimento:
    def __init__(self, id, descricao, desativado):
        """
        Inicializa um objeto TipoAtendimento com os atributos específicos.

        Args:
            id (int): Identificador único do tipo de atendimento.
            descricao (str): Descrição do tipo de atendimento.
            desativado (bool): Indica se o tipo de atendimento está desativado ou não.
        """
        self.id = id  # Identificador único do tipo de atendimento
        self.descricao = descricao  # Descrição do tipo de atendimento
        self.desativado = desativado  # Indica se o tipo de atendimento está desativado ou não

    def __str__(self):
        """
        Retorna uma representação em string do objeto TipoAtendimento.

        Returns:
            str: Representação em string do objeto TipoAtendimento.
        """
        return f"Tipo de Atendimento: ({self.id}) {self.descricao}"
