class Usuario:
    def __init__(self, id, nome, contato, email, funcao, desativado):
        """
        Inicializa um objeto Usuario com os atributos específicos.

        Args:
            id (int): Identificador único do usuário.
            nome (str): Nome do usuário.
            contato (str): Informações de contato do usuário.
            email (str): Endereço de e-mail do usuário.
            funcao (str): Função ou cargo do usuário.
            desativado (bool): Indica se o usuário está desativado ou não.
        """
        self.id = id  # Identificador único do usuário
        self.nome = nome  # Nome do usuário
        self.contato = contato  # Informações de contato do usuário
        self.email = email  # Endereço de e-mail do usuário
        self.funcao = funcao  # Função ou cargo do usuário
        self.desativado = desativado  # Indica se o usuário está desativado ou não

    def __str__(self):
        """
        Retorna uma representação em string do objeto Usuario.

        Returns:
            str: Representação em string do objeto Usuario.
        """
        return f"Usuário: ({self.id}) {self.nome}"
