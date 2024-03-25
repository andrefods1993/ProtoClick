from app.models.tipo_atendimento import TipoAtendimento
from app.controllers.message import Message
from app.managers.table_manager import TableManager
from app.commands.insert import Insert
from app.commands.update import Update
from app.commands.delete import Delete

class TypeController:
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
        self.tabela_manager = TableManager(tabela_tiposAtendimento=self.ui.tabela_tiposAtendimento)  # Gerenciamento da tabela de tipos de atendimento na interface

        # Conexão de sinais e slots para interação com a interface
        self.ui.btn_salvarCadastroTiposAtendimento.clicked.connect(self.cadastrar_tipo_atendimento)
        self.ui.btn_limparCadastroTiposAtendimento.clicked.connect(self.limpar_formulario_tipo_atendimento)
        self.ui.btn1_editarTiposAtendimento.clicked.connect(self.editar_tipo_atendimento)
        self.ui.btn2_excluirTiposAtendimento.clicked.connect(self.excluir_tipo_atendimento)

    def cadastrar_tipo_atendimento(self):
        """
        Método para cadastrar um novo tipo atendimento com base nos dados inseridos na interface.
        """
        # Obter os dados do formulário
        descricao = self.ui.ed_tiposAtendimentoDescricao.text()
        desativado = 'S' if self.ui.cb_tiposAtendimentoDesativado.isChecked() else 'N'

        if descricao:
            if self.ui.ed_tiposAtendimentoId.text():
                # Atualizar tipo de atendimento se o ID estiver presente
                id_tipo_atendimento = int(self.ui.ed_tiposAtendimentoId.text())
                tipo_atendimento = TipoAtendimento(
                    id=id_tipo_atendimento,
                    descricao=descricao,
                    desativado=desativado
                )

                self.update.atualizar_tipo_atendimento(tipo_atendimento)  # Atualiza o tipo de atendimento no banco de dados
                self.mensagem.mensagem_informacao(msg_title='Atualização Tipo de Atendimento', msg='Tipo de atendimento atualizado com sucesso!')
                self.ui.tabela_tiposAtendimento.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os tipos de atendimento na linha correta.
                self.limpar_formulario_tipo_atendimento()
                self.tabela_manager.carregar_tipos_atendimento()
            else:
                # Novo cadastro se não houver ID
                novo_tipo_atendimento = TipoAtendimento(
                    id=None,
                    descricao=descricao,
                    desativado=desativado
                )

                self.insert.inserir_tipo_atendimento(novo_tipo_atendimento)  # Insere o novo tipo de atendimento no banco de dados
                self.mensagem.mensagem_informacao(msg_title='Cadastro do Tipo de Atendimento', msg='Tipo de atendimento cadastrado com sucesso!')
                self.ui.tabela_tiposAtendimento.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os tipos de atendimento na linha correta.
                self.limpar_formulario_tipo_atendimento()
                self.tabela_manager.carregar_tipos_atendimento()
        else:
            self.mensagem.mensagem_aviso(msg_title='O cadastro falhou', msg='Por favor, preencha todos os campos obrigatórios do formulário.')


    def limpar_formulario_tipo_atendimento(self):
        """
        Limpa todos os campos do formulário de cadastro de tipo atendimento na interface.
        """
        self.ui.ed_tiposAtendimentoId.clear()
        self.ui.ed_tiposAtendimentoDescricao.clear()
        self.ui.cb_tiposAtendimentoDesativado.setChecked(False)
        self.ui.cb_tiposAtendimentoDesativado.setEnabled(False)  # Desabilita a edição do checkbox


    def editar_tipo_atendimento(self):
        """
        Método para editar um tipo de atendimento existente com base na seleção na tabela de tipoAtendimento.
        """
        if self.ui.tabela_tiposAtendimento.selectedItems():
            row = self.ui.tabela_tiposAtendimento.currentRow()
            id_tipo_atendimento = int(self.ui.tabela_tiposAtendimento.item(row, 0).text())
            descricao = self.ui.tabela_tiposAtendimento.item(row, 1).text()
            desativado = self.ui.tabela_tiposAtendimento.item(row, 2).text()

            # Preenche os campos do formulário de edição com os dados do tipo de atendimento selecionado
            self.ui.ed_tiposAtendimentoId.setText(str(id_tipo_atendimento))
            self.ui.ed_tiposAtendimentoDescricao.setText(descricao)

            # Configura o estado do checkbox de desativado baseado no valor obtido
            self.ui.cb_tiposAtendimentoDesativado.setChecked(True if desativado == 'S' else False)

            self.ui.cb_tiposAtendimentoDesativado.setEnabled(True)  # Habilita a edição do checkbox
            self.ui.aba_tipos_atendimento.setCurrentIndex(1)  # Altera a aba para a de edição
        else:
            self.mensagem.mensagem_aviso(msg_title='A edição falhou', msg='Por favor, selecione um tipo de atendimento na tabela para editar.')


    def excluir_tipo_atendimento(self):
        """
        Método para excluir um tipo de atendimento existente com base na seleção na tabela de tipoAtendimento.
        """
        if self.ui.tabela_tiposAtendimento.selectedItems():
            row = self.ui.tabela_tiposAtendimento.currentRow()
            id_tipo_atendimento = int(self.ui.tabela_tiposAtendimento.item(row, 0).text())

            # Confirma a exclusão de tipo atendimento através do comando de delete
            self.delete.confirmar_exclusao_tipo_atendimento(id_tipo_atendimento)
            self.ui.tabela_tiposAtendimento.sortItems(0)  # Ordena a tabela pelo ID (coluna 0), #? Para carregar os tipos de atendimento na linha correta.
            self.limpar_formulario_tipo_atendimento()
            self.tabela_manager.carregar_tipos_atendimento()
        else:
            self.mensagem.mensagem_aviso(msg_title='A exclusão falhou', msg='Por favor, selecione um tipo de atendimento na tabela para excluir.')
