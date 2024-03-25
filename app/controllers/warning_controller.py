from app.models.aviso import Aviso
from app.controllers.message import Message
from app.managers.table_manager import TableManager
from app.commands.insert import Insert
from app.commands.update import Update
from app.commands.delete import Delete

class WarningController:
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
        self.tabela_manager = TableManager(tabela_avisos=self.ui.tabela_avisos)  # Gerenciamento da tabela de avisos na interface

        # Conexão de sinais e slots para interação com a interface
        self.ui.btn_salvarCadastroAvisos.clicked.connect(self.cadastrar_aviso)
        self.ui.btn_limparCadastroAvisos.clicked.connect(self.limpar_formulario_aviso)
        self.ui.btn1_editarAvisos.clicked.connect(self.editar_aviso)
        self.ui.btn2_excluirAvisos.clicked.connect(self.excluir_aviso)


    def cadastrar_aviso(self):
        """
        Método para cadastrar um novo aviso com base nos dados inseridos na interface.
        """
        # Obter os dados do formulário
        descricao = self.ui.ed_avisosDescricao.text()
        mensagem = self.ui.ed_avisosMensagem.toPlainText()
        desativado = 'S' if self.ui.cb_avisosDesativado.isChecked() else 'N'

        if descricao and mensagem:
            if self.ui.ed_avisosId.text():
                # Atualizar avisos se o ID estiver presente
                id_aviso = int(self.ui.ed_avisosId.text())
                aviso = Aviso(
                    id=id_aviso,
                    descricao=descricao,
                    mensagem=mensagem,
                    desativado=desativado
                )

                self.update.atualizar_aviso(aviso)  # Atualiza o aviso no banco de dados
                self.mensagem.mensagem_informacao(msg_title='Atualização de Aviso', msg='Aviso atualizado com sucesso!')
                self.ui.tabela_avisos.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os avisos na linha correta.
                self.limpar_formulario_aviso()
                self.tabela_manager.carregar_avisos()
            else:
                # Novo cadastro se não houver ID
                novo_aviso = Aviso(
                    id=None,
                    descricao=descricao,
                    mensagem=mensagem,
                    desativado=desativado
                )

                self.insert.inserir_aviso(novo_aviso)  # Insere o novo aviso no banco de dados
                self.mensagem.mensagem_informacao(msg_title='Cadastro do Aviso', msg='Aviso cadastrado com sucesso!')
                self.ui.tabela_avisos.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os avisos na linha correta.
                self.limpar_formulario_aviso()
                self.tabela_manager.carregar_avisos()
        else:
            self.mensagem.mensagem_aviso(msg_title='O cadastro falhou', msg='Por favor, preencha todos os campos obrigatórios do formulário.')


    def limpar_formulario_aviso(self):
        """
        Limpa todos os campos do formulário de cadastro do aviso na interface.
        """
        self.ui.ed_avisosId.clear()
        self.ui.ed_avisosDescricao.clear()
        self.ui.ed_avisosMensagem.clear()
        self.ui.cb_avisosDesativado.setChecked(False)
        self.ui.cb_avisosDesativado.setEnabled(False)  # Desabilita a edição do checkbox


    def editar_aviso(self):
        """
        Método para editar um aviso existente com base na seleção na tabela de avisos.
        """
        if self.ui.tabela_avisos.selectedItems():
            row = self.ui.tabela_avisos.currentRow()
            id_aviso = int(self.ui.tabela_avisos.item(row, 0).text())
            descricao = self.ui.tabela_avisos.item(row, 1).text()
            mensagem = self.ui.tabela_avisos.item(row, 2).text()
            desativado = self.ui.tabela_avisos.item(row, 3).text()

            # Preenche os campos do formulário de edição com os dados do aviso selecionado
            self.ui.ed_avisosId.setText(str(id_aviso))
            self.ui.ed_avisosDescricao.setText(descricao)
            self.ui.ed_avisosMensagem.setText(mensagem)

            # Configura o estado do checkbox de desativado baseado no valor obtido
            self.ui.cb_avisosDesativado.setChecked(True if desativado == 'S' else False)

            self.ui.cb_avisosDesativado.setEnabled(True)  # Habilita a edição do checkbox
            self.ui.aba_avisos.setCurrentIndex(1)  # Altera a aba para a de edição
        else:
            self.mensagem.mensagem_aviso(msg_title='A edição falhou', msg='Por favor, selecione um aviso na tabela para editar.')


    def excluir_aviso(self):
        """
        Método para excluir um aviso existente com base na seleção na tabela de avisos.
        """
        if self.ui.tabela_avisos.selectedItems():
            row = self.ui.tabela_avisos.currentRow()
            id_aviso = int(self.ui.tabela_avisos.item(row, 0).text())

            # Confirma a exclusão de aviso através do comando de delete
            self.delete.confirmar_exclusao_aviso(id_aviso)
            self.ui.tabela_avisos.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os avisos na linha correta.
            self.limpar_formulario_aviso()
            self.tabela_manager.carregar_avisos()
        else:
            self.mensagem.mensagem_aviso(msg_title='A exclusão falhou', msg='Por favor, selecione um aviso na tabela para excluir.')
