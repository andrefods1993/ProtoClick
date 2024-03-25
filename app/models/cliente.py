class Cliente:
    def __init__(self, id, razao_social, cpf_cnpj, natureza_social, contato, email, solicitante,
                 cep, logradouro, numero, bairro, cidade, uf, referencia, desativado):
        """
        Inicializa um objeto Cliente com os atributos específicos.

        Args:
            id (int): Identificador único do cliente.
            razao_social (str): Razão social do cliente.
            cpf_cnpj (str): CPF ou CNPJ do cliente.
            natureza_social (str): Natureza social do cliente (pessoa física ou jurídica).
            contato (str): Informações de contato do cliente.
            email (str): Endereço de e-mail do cliente.
            solicitante (str): Solicitante responsável pelo cliente.
            cep (str): CEP do cliente.
            logradouro (str): Logradouro do cliente.
            numero (int): Número do endereço do cliente.
            bairro (str): Bairro do cliente.
            cidade (str): Cidade do cliente.
            uf (str): Estado do cliente.
            referencia (str): Referência do endereço do cliente.
            desativado (str): Indica se o cliente está desativado ('S' ou 'N').
        """
        self.id = id  # Identificador único do cliente
        self.razao_social = razao_social  # Razão social do cliente
        self.cpf_cnpj = cpf_cnpj  # CPF ou CNPJ do cliente
        self.natureza_social = natureza_social  # Natureza social do cliente (pessoa física ou jurídica)
        self.contato = contato  # Informações de contato do cliente
        self.email = email  # Endereço de e-mail do cliente
        self.solicitante = solicitante  # Solicitante responsável pelo cliente
        self.cep = cep  # CEP do cliente
        self.logradouro = logradouro  # Logradouro do cliente
        self.numero = numero  # Número do endereço do cliente
        self.bairro = bairro  # Bairro do cliente
        self.cidade = cidade  # Cidade do cliente
        self.uf = uf  # Estado do cliente
        self.referencia = referencia  # Referência do endereço do cliente
        self.desativado = desativado  # Indica se o cliente está desativado ('S' ou 'N')

    def __str__(self):
        """
        Retorna uma representação em string do objeto Cliente.

        Returns:
            str: Representação em string do objeto Cliente.
        """
        return f"Cliente: ({self.id}) {self.razao_social}"
