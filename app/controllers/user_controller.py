from app.models.usuario import Usuario
from app.controllers.message import Message
from app.managers.table_manager import TableManager
from app.commands.insert import Insert
from app.commands.update import Update
from app.commands.delete import Delete

class UserController:
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
        self.tabela_manager = TableManager(tabela_usuarios=self.ui.tabela_usuarios)  # Gerenciamento da tabela de usuários na interface

        # Conexão de sinais e slots para interação com a interface
        self.ui.btn_salvarCadastroUsurios.clicked.connect(self.cadastrar_usuario)
        self.ui.btn_limparCadastroUsuarios.clicked.connect(self.limpar_formulario_usuario)
        self.ui.btn1_editarUsuarios.clicked.connect(self.editar_usuario)
        self.ui.btn2_excluirUsuarios.clicked.connect(self.excluir_usuario)


    def cadastrar_usuario(self):
        """
        Método para cadastrar um novo usuário com base nos dados inseridos na interface.
        """
        # Obter os dados do formulário
        nome = self.ui.ed_usuariosNome.text()
        contato = self.ui.ed_usuariosContato.text()
        email = self.ui.ed_usuariosEmail.text()
        funcao = self.ui.ed_usuariosFuncao.text()
        desativado = 'S' if self.ui.cb_usuariosDesativado.isChecked() else 'N'

        if nome and contato and email and funcao:
            if self.ui.ed_usuarioId.text():
                # Atualizar usuário se o ID estiver presente
                id_usuario = int(self.ui.ed_usuarioId.text())
                usuario = Usuario(
                    id=id_usuario,
                    nome=nome,
                    contato=contato,
                    email=email,
                    funcao=funcao,
                    desativado=desativado
                )

                self.update.atualizar_usuario(usuario)  # Atualiza o usuário no banco de dados
                self.mensagem.mensagem_informacao(msg_title='Atualização de Usuário', msg='Usuário atualizado com sucesso!')
                self.ui.tabela_usuarios.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os usuários na linha correta.
                self.limpar_formulario_usuario()
                self.tabela_manager.carregar_usuarios()
            else:
                # Novo cadastro se não houver ID
                novo_usuario = Usuario(
                    id=None,
                    nome=nome,
                    contato=contato,
                    email=email,
                    funcao=funcao,
                    desativado=desativado
                )

                self.insert.inserir_usuario(novo_usuario)  # Insere o novo usuário no banco de dados
                self.mensagem.mensagem_informacao(msg_title='Cadastro de Usuário', msg='Usuário cadastrado com sucesso!')
                self.ui.tabela_usuarios.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os usuários na linha correta.
                self.limpar_formulario_usuario()
                self.tabela_manager.carregar_usuarios()
        else:
            self.mensagem.mensagem_aviso(msg_title='O cadastro falhou', msg='Por favor, preencha todos os campos obrigatórios do formulário.')


    def limpar_formulario_usuario(self):
        """
        Limpa todos os campos do formulário de cadastro de usuários na interface.
        """
        self.ui.ed_usuarioId.clear()
        self.ui.ed_usuariosNome.clear()
        self.ui.ed_usuariosContato.clear()
        self.ui.ed_usuariosEmail.clear()
        self.ui.ed_usuariosFuncao.clear()
        self.ui.cb_usuariosDesativado.setChecked(False)
        self.ui.cb_usuariosDesativado.setEnabled(False)  # Desabilita a edição do checkbox


    def editar_usuario(self):
        """
        Método para editar um usuário existente com base na seleção na tabela de usuários.
        """
        if self.ui.tabela_usuarios.selectedItems():
            row = self.ui.tabela_usuarios.currentRow()
            id_usuario = int(self.ui.tabela_usuarios.item(row, 0).text())
            nome = self.ui.tabela_usuarios.item(row, 1).text()
            contato = self.ui.tabela_usuarios.item(row, 2).text()
            email = self.ui.tabela_usuarios.item(row, 3).text()
            funcao = self.ui.tabela_usuarios.item(row, 4).text()
            desativado = self.ui.tabela_usuarios.item(row, 5).text()

            # Preenche os campos do formulário de edição com os dados do usuário selecionado
            self.ui.ed_usuarioId.setText(str(id_usuario))
            self.ui.ed_usuariosNome.setText(nome)
            self.ui.ed_usuariosContato.setText(contato)
            self.ui.ed_usuariosEmail.setText(email)
            self.ui.ed_usuariosFuncao.setText(funcao)

            # Configura o estado do checkbox de desativado baseado no valor obtido
            self.ui.cb_usuariosDesativado.setChecked(True if desativado == 'S' else False)

            self.ui.cb_usuariosDesativado.setEnabled(True)  # Habilita a edição do checkbox
            self.ui.aba_usuarios.setCurrentIndex(1)  # Altera a aba para a de edição
        else:
            self.mensagem.mensagem_aviso(msg_title='A edição falhou', msg='Por favor, selecione um usuário na tabela para editar.')


    def excluir_usuario(self):
        """
        Método para excluir um usuário existente com base na seleção na tabela de usuários.
        """
        if self.ui.tabela_usuarios.selectedItems():
            row = self.ui.tabela_usuarios.currentRow()
            id_usuario = int(self.ui.tabela_usuarios.item(row, 0).text())

            # Confirma a exclusão do usuário através do comando de delete
            self.delete.confirmar_exclusao_usuario(id_usuario)
            self.ui.tabela_usuarios.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os usuários na linha correta.
            self.limpar_formulario_usuario()
            self.tabela_manager.carregar_usuarios()
        else:
            self.mensagem.mensagem_aviso(msg_title='A exclusão falhou', msg='Por favor, selecione um usuário na tabela para excluir.')
