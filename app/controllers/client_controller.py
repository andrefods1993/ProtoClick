from app.models.cliente import Cliente
from app.controllers.message import Message
from app.managers.table_manager import TableManager
from app.commands.insert import Insert
from app.commands.update import Update
from app.commands.delete import Delete

class ClientController:
    def __init__(self, ui):
        """
        Controlador responsável pela lógica de interação com os usuários na interface.

        Args:
            ui: Objeto de interface do usuário.
        """
        self.ui = ui  # Objeto de interface

        # Instância dos objetos necessários para manipulação de dados
        self.insert = Insert()  # Comando de inserção no banco de dados
        self.update = Update()  # Comando de atualização no banco de dados
        self.delete = Delete()  # Comando de exclusão no banco de dados
        self.mensagem = Message()  # Gerenciamento de mensagens exibidas ao usuário
        self.tabela_manager = TableManager(tabela_clientes=self.ui.tabela_clientes)  # Gerenciamento da tabela de clientes na interface

        # Conexão de sinais e slots para interação com a interface
        self.ui.btn_salvarCadastroClientes.clicked.connect(self.cadastrar_cliente)
        self.ui.btn_limparCadastroClientes.clicked.connect(self.limpar_formulario_cliente)
        self.ui.btn1_editarClientes.clicked.connect(self.editar_cliente)
        self.ui.btn2_excluirClientes.clicked.connect(self.excluir_cliente)


    def cadastrar_cliente(self):
        """
        Método para cadastrar um novo cliente com base nos dados inseridos na interface.
        """
        # Obter os dados do formulário
        razao_social = self.ui.ed_clientesRazaoSocial.text()
        cpf_cnpj = self.ui.ed_clientesCpfCnpj.text()
        natureza_social = "Jurídica" if self.ui.rd_clientesJuridica.isChecked() else "Física"
        contato = self.ui.ed_clientesContato.text()
        email = self.ui.ed_clientesEmail.text()
        solicitante = self.ui.ed_clientesSolicitante.text()
        cep = self.ui.ed_enderecoClientesCep.text()
        logradouro = self.ui.ed_enderecoClientesLodradouro.text()
        numero = self.ui.ed_enderecoClientesNumeros.text()
        bairro = self.ui.ed_enderecoClienteBairro.text()
        cidade = self.ui.cb_enderecoClientesCidade.currentText()
        uf = self.ui.cb_enderecoClientesUF.currentText()
        referencia = self.ui.ed_enderecoClientesReferencia.text()
        desativado = 'S' if self.ui.cb_usuariosDesativado.isChecked() else 'N'

        if (razao_social and cpf_cnpj and natureza_social and contato and solicitante and
            cep and logradouro and numero and bairro and cidade and uf):
            if self.ui.ed_clientesId.text():
                # Atualizar cliente se o ID estiver presente
                id_cliente = int(self.ui.ed_clientesId.text())
                cliente = Cliente(
                    id=id_cliente,
                    razao_social=razao_social,
                    cpf_cnpj=cpf_cnpj,
                    natureza_social= natureza_social,
                    contato=contato,
                    email=email,
                    solicitante=solicitante,
                    cep=cep,
                    logradouro=logradouro,
                    numero=numero,
                    bairro=bairro,
                    cidade=cidade,
                    uf=uf,
                    referencia=referencia,
                    desativado=desativado
                )

                self.update.atualizar_cliente(cliente)  # Atualiza o cliente no banco de dados
                self.mensagem.mensagem_informacao(msg_title='Atualização de Cliente', msg='Cliente atualizado com sucesso!')
                self.ui.tabela_clientes.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os clientes na linha correta.
                self.limpar_formulario_cliente()
                self.tabela_manager.carregar_clientes()
            else:
                # Novo cadastro se não houver ID
                novo_cliente = Cliente(
                    id=None,
                    razao_social=razao_social,
                    cpf_cnpj=cpf_cnpj,
                    natureza_social= natureza_social,
                    contato=contato,
                    email=email,
                    solicitante=solicitante,
                    cep=cep,
                    logradouro=logradouro,
                    numero=numero,
                    bairro=bairro,
                    cidade=cidade,
                    uf=uf,
                    referencia=referencia,
                    desativado=desativado
                )

                self.insert.inserir_cliente(novo_cliente)  # Insere o novo cliente no banco de dados
                self.mensagem.mensagem_informacao(msg_title='Cadastro de Cliente', msg='Cliente cadastrado com sucesso!')
                self.ui.tabela_clientes.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os clientes na linha correta.
                self.limpar_formulario_cliente()
                self.tabela_manager.carregar_clientes()
        else:
            self.mensagem.mensagem_aviso(msg_title='O cadastro falhou', msg='Por favor, preencha todos os campos obrigatórios do formulário.')


    def limpar_formulario_cliente(self):
        """
        Limpa todos os campos do formulário de cadastro de cliente na interface.
        """
        self.ui.ed_clientesId.clear()
        self.ui.ed_clientesRazaoSocial.clear()
        self.ui.ed_clientesCpfCnpj.clear()
        self.ui.ed_clientesContato.clear()
        self.ui.ed_clientesEmail.clear()
        self.ui.ed_clientesSolicitante.clear()
        self.ui.ed_enderecoClientesCep.clear()
        self.ui.ed_enderecoClientesLodradouro.clear()
        self.ui.ed_enderecoClientesNumeros.clear()
        self.ui.ed_enderecoClienteBairro.clear()
        self.ui.ed_enderecoClientesReferencia.clear()
        self.ui.cb_enderecoClientesUF.setCurrentText('AC')
        self.ui.rd_clientesJuridica.setChecked(True)
        self.ui.cd_clientesDesativado.setChecked(False)
        self.ui.cd_clientesDesativado.setEnabled(False)  # Desabilita a edição do checkbox


    def editar_cliente(self):
        """
        Método para editar um cliente existente com base na seleção na tabela de usuários.
        """
        if self.ui.tabela_clientes.selectedItems():
            row = self.ui.tabela_clientes.currentRow()
            id_cliente = int(self.ui.tabela_clientes.item(row, 0).text())
            razao_social = self.ui.tabela_clientes.item(row, 1).text()
            cpf_cnpj = self.ui.tabela_clientes.item(row, 2).text()
            natureza_social = self.ui.tabela_clientes.item(row, 3).text()
            contato = self.ui.tabela_clientes.item(row, 4).text()
            email = self.ui.tabela_clientes.item(row, 5).text()
            solicitante = self.ui.tabela_clientes.item(row, 6).text()
            cep = self.ui.tabela_clientes.item(row, 7).text()
            logradouro = self.ui.tabela_clientes.item(row, 8).text()
            numero = self.ui.tabela_clientes.item(row, 9).text()
            bairro = self.ui.tabela_clientes.item(row, 10).text()
            cidade = self.ui.tabela_clientes.item(row, 11).text()
            uf = self.ui.tabela_clientes.item(row, 12).text()
            referencia = self.ui.tabela_clientes.item(row, 13).text()
            desativado = self.ui.tabela_clientes.item(row, 14).text()

            # Preenche os campos do formulário de edição com os dados do cliente selecionado
            self.ui.ed_clientesId.setText(str(id_cliente))  # Convertido para string
            self.ui.ed_clientesRazaoSocial.setText(razao_social)
            self.ui.ed_clientesCpfCnpj.setText(cpf_cnpj)
            self.ui.ed_clientesContato.setText(contato)
            self.ui.ed_clientesEmail.setText(email)
            self.ui.ed_clientesSolicitante.setText(solicitante)
            self.ui.ed_enderecoClientesCep.setText(cep)
            self.ui.ed_enderecoClientesLodradouro.setText(logradouro)
            self.ui.ed_enderecoClientesNumeros.setText(numero)
            self.ui.ed_enderecoClienteBairro.setText(bairro)
            self.ui.cb_enderecoClientesCidade.setCurrentText(cidade)  # Define o texto selecionado no ComboBox de cidade
            self.ui.cb_enderecoClientesUF.setCurrentText(uf)  # Define o texto selecionado no ComboBox de UF
            self.ui.ed_enderecoClientesReferencia.setText(referencia)
            
            if natureza_social == "Jurídica":
                self.ui.rd_clientesJuridica.setChecked(True)  # Marca o RadioButton Jurídica se a natureza for jurídica
            else:
                self.ui.rd_clientesFisica.setChecked(True)  # Marca o RadioButton Física se a natureza for física
            
            # Configura o estado do checkbox de desativado baseado no valor obtido
            self.ui.cd_clientesDesativado.setChecked(True if desativado == 'S' else False)

            self.ui.cd_clientesDesativado.setEnabled(True)  # Habilita a edição do checkbox
            self.ui.aba_clientes.setCurrentIndex(1)  # Altera a aba para a de edição
        else:
            self.mensagem.mensagem_aviso(msg_title='A edição falhou', msg='Por favor, selecione um cliente na tabela para editar.')


    def excluir_cliente(self):
        """
        Método para excluir um cliente existente com base na seleção na tabela de clientes.
        """
        if self.ui.tabela_clientes.selectedItems():
            row = self.ui.tabela_clientes.currentRow()
            id_cliente = int(self.ui.tabela_clientes.item(row, 0).text())

            # Confirma a exclusão do cliente através do comando de delete
            self.delete.confirmar_exclusao_cliente(id_cliente)
            self.ui.tabela_clientes.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os clientes na linha correta.
            self.limpar_formulario_cliente()
            self.tabela_manager.carregar_clientes()
        else:
            self.mensagem.mensagem_aviso(msg_title='A exclusão falhou', msg='Por favor, selecione um cliente na tabela para excluir.')
