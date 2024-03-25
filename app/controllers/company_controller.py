import base64
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFileDialog

from app.models.empresa import Empresa
from app.controllers.message import Message
from app.managers.empresa_manager import EmpresaManager
from app.commands.insert import Insert
from app.commands.update import Update
from app.commands.delete import Delete

class CompanyController:
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
        self.empresa_manager = EmpresaManager(self.ui)  # Gerenciamento da empresa na interface

        # Conexão de sinais e slots para interação com a interface
        self.ui.btn_salvarEmpresa.clicked.connect(self.salvar_empresa)
        self.ui.btn_editarEmpresa.clicked.connect(self.editar_empresa)
        self.ui.btn_excluirEmpresa.clicked.connect(self.excluir_empresa)
        self.ui.btn_selecionarLogoEmpresa.clicked.connect(self.selecionar_logo)
        self.ui.btn_removerLogoEmpresa.clicked.connect(self.excluir_logo)


    def salvar_empresa(self):
        """
        Método para cadastrar um nova empresa com base nos dados inseridos na interface.
        """
        # Obter os dados do formulário
        razao_social = self.ui.ed_empresaRazaoSocial.text()
        cpf_cnpj = self.ui.ed_empresaCpfCnpj.text()
        contato = self.ui.ed_empresaContato.text()
        email = self.ui.ed_empresaEmail.text()
        endereco_cep = self.ui.ed_empresaCep.text()
        endereco_logradouro = self.ui.ed_empresaLogradouro.text()
        endereco_numero = self.ui.ed_empresaNumero.text()
        endereco_bairro = self.ui.ed_empresaBairro.text()
        endereco_referencia = self.ui.ed_empresaReferencia.text()
        uf = self.ui.cb_empresaUf.currentText()
        cidade = self.ui.cb_empresaCidade.currentText()
        natureza_social = "Jurídica" if self.ui.radioButton_empresaJuridica.isChecked() else "Física"

        if (razao_social and cpf_cnpj and natureza_social and contato and email and
            endereco_cep and endereco_logradouro and endereco_numero and
            endereco_bairro and cidade and uf):
            if self.ui.ed_empresaId.text():
                # Atualizar empresa se o ID estiver presente
                id_empresa = int(self.ui.ed_empresaId.text())
                empresa = Empresa(
                    id=id_empresa,
                    razao_social=razao_social,
                    cpf_cnpj=cpf_cnpj,
                    natureza_social=natureza_social,
                    contato=contato,
                    email=email,
                    logo=None,
                    endereco_cep=endereco_cep,
                    endereco_logradouro=endereco_logradouro,
                    endereco_numero=endereco_numero,
                    endereco_bairro=endereco_bairro,
                    endereco_referencia=endereco_referencia,
                    cidade=cidade,
                    uf=uf
                )

                self.update.atualizar_empresa(empresa)  # Atualiza o empresa no banco de dados
                if self.ui.ed_empresaRazaoSocial.isReadOnly():
                    self.mensagem.mensagem_aviso(msg_title='A atualização falhou', msg='Clique em "Editar" antes de fazer a atualização.')
                    return
                self.mensagem.mensagem_informacao(msg_title='Atualização da empresa', msg='Empresa atualizado com sucesso!')
                self.empresa_manager.carregar_empresa()
            else:
                # Novo cadastro se não houver ID
                novo_empresa = Empresa(
                    id=None,
                    razao_social=razao_social,
                    cpf_cnpj=cpf_cnpj,
                    natureza_social=natureza_social,
                    contato=contato,
                    email=email,
                    logo=None,
                    endereco_cep=endereco_cep,
                    endereco_logradouro=endereco_logradouro,
                    endereco_numero=endereco_numero,
                    endereco_bairro=endereco_bairro,
                    endereco_referencia=endereco_referencia,
                    cidade=cidade,
                    uf=uf
                )

                self.insert.inserir_empresa(novo_empresa)  # Insere a nova empresa no banco de dados
                self.mensagem.mensagem_informacao(msg_title='Cadastro da Empresa', msg='Empresa cadastrada com sucesso!')
                self.empresa_manager.carregar_empresa()
        else:
            self.mensagem.mensagem_aviso(msg_title='O cadastro falhou', msg='Por favor, preencha todos os campos obrigatórios do formulário.')


    def editar_empresa(self):
        """
        Método para editar um empresa existente com base na seleção na tabela de usuários.
        """
        if self.ui.ed_empresaId.text():
            # Desbloquear a edição dos campos de texto
            self.ui.ed_empresaRazaoSocial.setReadOnly(False)
            self.ui.ed_empresaCpfCnpj.setReadOnly(False)
            self.ui.ed_empresaContato.setReadOnly(False)
            self.ui.ed_empresaEmail.setReadOnly(False)
            self.ui.ed_empresaCep.setReadOnly(False)
            self.ui.ed_empresaLogradouro.setReadOnly(False)
            self.ui.ed_empresaNumero.setReadOnly(False)
            self.ui.ed_empresaBairro.setReadOnly(False)
            self.ui.ed_empresaReferencia.setReadOnly(False)

            # Desbloquear a seleção dos combo boxes
            self.ui.cb_empresaUf.setEnabled(True)
            self.ui.cb_empresaCidade.setEnabled(True)

            # Desbloquear a seleção dos radio buttons
            self.ui.radioButton_empresaJuridica.setEnabled(True)
            self.ui.radioButton_empresaFisica.setEnabled(True)
        else:
            self.mensagem.mensagem_aviso(msg_title='A edição falhou', msg='Não tem empresa para editar.')


    def excluir_empresa(self):
        """
        Método para excluir um empresa existente com base.
        """
        if self.ui.ed_empresaId.text():
            # Confirma a exclusão do empresa através do comando de delete
            id_empresa = int(self.ui.ed_empresaId.text())
            confirmacao = self.delete.confirmar_exclusao_empresa(id_empresa)

            if confirmacao == 'Yes':
                self.limpar_formulario_empresa()
        else:
            self.mensagem.mensagem_aviso(msg_title='A exclusão falhou', msg='Não tem empresa para excluir.')


    def selecionar_logo(self):
        """
        Método para selecionar uma logo para empresa com base nos dados inseridos na interface.
        """
        if not self.ui.ed_empresaId.text():
            self.mensagem.mensagem_aviso(msg_title='Aviso', msg='Por favor, cadastre uma empresa antes de adicionar uma logo.')
            return

        file_dialog = QFileDialog()
        file_dialog.setWindowTitle('Selecionar Imagem')
        file_dialog.setNameFilter('Imagens (*.png *.jpg *.jpeg *.bmp *.gif)')
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)  # Define o modo de seleção como seleção de arquivo existente

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]

            # Verificar o tamanho da imagem
            pixmap = QPixmap(file_path)
            width = pixmap.width()
            height = pixmap.height()

            if not (100 <= width <= 400 and 100 <= height <= 400):
                self.mensagem.mensagem_aviso(msg_title='Aviso', msg='A imagem deve ter tamanho mínimo de 100x100 e máximo de 400x400 pixels.')
                return

            id_empresa = self.ui.ed_empresaId.text()

            # Converte a imagem para bytes em formato base64
            with open(file_path, 'rb') as img_file:
                imagem_bytes = img_file.read()
                imagem_base64 = base64.b64encode(imagem_bytes).decode('utf-8')

            # Exibir a imagem no QLabel da interface
            self.ui.logoEmpresa.setPixmap(pixmap)
            self.ui.logoEmpresa.setScaledContents(True)  # Redimensiona a imagem para caber na label

            self.update.atualizar_logo(imagem_base64, id_empresa)  # Atualizar logo da empresa no banco de dados
            self.mensagem.mensagem_informacao(msg_title='Atualização de Logo', msg='Logo Atualizada com sucesso!')
            self.empresa_manager.carregar_empresa()
        
        else:
            self.mensagem.mensagem_aviso(msg_title='A atualização falhou', msg='Por favor, selecione uma imagem válida (entre 100x100 e 400x400 pixels).')
    
    
    def excluir_logo(self):
        """
        Método para excluir uma logo existente com base.
        """
        if self.ui.ed_empresaId.text():
            # Confirma a exclusão do empresa através do comando de delete
            id_empresa = int(self.ui.ed_empresaId.text())
            confirmacao = self.delete.confirmar_exclusao_logo(id_empresa)
            if confirmacao == 'Yes':
                default_image_path = 'assets/icons/logo_p_dark_200px.png'
                pixmap = QPixmap(default_image_path)
                self.ui.logoEmpresa.setPixmap(pixmap)
                self.ui.logoEmpresa.setScaledContents(True)  # Redimensiona a imagem para caber na label
            self.empresa_manager.carregar_empresa()
        else:
            self.mensagem.mensagem_aviso(msg_title='A exclusão falhou', msg='Não tem empresa para excluir.')


    def limpar_formulario_empresa(self):
        """
        Método para limpar todos os campos do formulário após a exclusão da empresa.
        """
        self.ui.ed_empresaId.clear()
        self.ui.ed_empresaRazaoSocial.clear()
        self.ui.ed_empresaCpfCnpj.clear()
        self.ui.ed_empresaContato.clear()
        self.ui.ed_empresaEmail.clear()
        self.ui.ed_empresaCep.clear()
        self.ui.ed_empresaLogradouro.clear()
        self.ui.ed_empresaNumero.clear()
        self.ui.ed_empresaBairro.clear()
        self.ui.ed_empresaReferencia.clear()
        self.ui.cb_empresaUf.setCurrentText('AC')
        self.ui.radioButton_empresaJuridica.setChecked(True)

        # Desbloquear a edição dos campos de texto
        self.ui.ed_empresaRazaoSocial.setReadOnly(False)
        self.ui.ed_empresaCpfCnpj.setReadOnly(False)
        self.ui.ed_empresaContato.setReadOnly(False)
        self.ui.ed_empresaEmail.setReadOnly(False)
        self.ui.ed_empresaCep.setReadOnly(False)
        self.ui.ed_empresaLogradouro.setReadOnly(False)
        self.ui.ed_empresaNumero.setReadOnly(False)
        self.ui.ed_empresaBairro.setReadOnly(False)
        self.ui.ed_empresaReferencia.setReadOnly(False)

        # Desbloquear a seleção dos combo boxes
        self.ui.cb_empresaUf.setEnabled(True)
        self.ui.cb_empresaCidade.setEnabled(True)

        # Desbloquear a seleção dos radio buttons
        self.ui.radioButton_empresaJuridica.setEnabled(True)
        self.ui.radioButton_empresaFisica.setEnabled(True)

        default_image_path = 'assets/icons/logo_p_dark_200px.png'
        pixmap = QPixmap(default_image_path)
        self.ui.logoEmpresa.setPixmap(pixmap)
        self.ui.logoEmpresa.setScaledContents(True)  # Redimensiona a imagem para caber na label