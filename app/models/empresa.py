class Empresa:
    def __init__(self, id, razao_social, natureza_social, cpf_cnpj, contato, email,
                 logo, endereco_cep, endereco_logradouro, endereco_numero, 
                 endereco_bairro, endereco_referencia, cidade, uf):
        """
        Inicializa um objeto Empresa com os atributos específicos.

        Args:
            id (int): Identificador único do empresa.
            razao_social (str): Razão social da empresa.
            cpf_cnpj (str): CPF ou CNPJ da empresa.
            natureza_social (str): Natureza social da empresa (pessoa física ou jurídica).
            contato (str): Informações de contato da empresa.
            email (str): Endereço de e-mail da empresa.
            logo (blob): Logo da empresa.
            endereco_cep (str): CEP da empresa.
            endereco_logradouro (str): Logradouro  da empresa .
            endereco_numero (str): Número do endereço da empresa.
            endereco_bairro (str): Bairro da empresa.
            endereco_referencia (str): Referência do endereço da empresa.
            cidade (str): Cidade da empresa.
            uf (str): Estado da empresa.
        """
        self.id = id  # Identificador único do empresa.
        self.razao_social = razao_social  # Razão social da empresa.
        self.cpf_cnpj = cpf_cnpj  # CPF ou CNPJ da empresa.
        self.natureza_social = natureza_social  # Natureza social da empresa (pessoa física ou jurídica).
        self.contato = contato  # Informações de contato da empresa.
        self.email = email  # Endereço de e-mail da empresa.
        self.logo = logo  # Logo da empresa.
        self.endereco_cep = endereco_cep  # CEP da empresa.
        self.endereco_logradouro = endereco_logradouro  # Logradouro  da empresa .
        self.endereco_numero = endereco_numero  # Número do endereço da empresa.
        self.endereco_bairro = endereco_bairro  # Bairro da empresa.
        self. endereco_referencia = endereco_referencia  # Referência do endereço da empresa.
        self.cidade = cidade  # Cidade da empresa.
        self.uf = uf  # Estado da empresa.

    def __str__(self):
        """
        Retorna uma representação em string do objeto Empresa.

        Returns:
            str: Representação em string do objeto Empresa.
        """
        return f"Empresa: ({self.id}) {self.razao_social}"
