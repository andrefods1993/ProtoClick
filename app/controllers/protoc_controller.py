from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QDate, QTime, QDir
import subprocess
from datetime import datetime
from app.models.protocolo import Protocolo
from app.controllers.message import Message
from app.managers.table_manager import TableManager
from app.commands.insert import Insert
from app.commands.update import Update
from app.commands.delete import Delete

from app.commands.report import gerar_relatorio_protocolo_word
from app.widgets.conversor_pdf import ConverterPDFThread
from app.widgets.whatsapp import upload_arquivo_e_enviar_whatsapp

class ProtocController:
    def __init__(self, ui):
        """
        Inicializa o controlador ProtocController.

        Args:
            ui: Objeto de interface do usuário.
        """
        self.ui = ui  # Atribui o objeto de interface do usuário à variável self.ui
        
        # Instância dos objetos necessários para manipulação de dados
        self.insert = Insert()
        self.update = Update()
        self.delete = Delete()
        self.mensagem = Message()
        self.tabela_manager = TableManager(tabela_protocolos=self.ui.tabela_protocolos)  # Instância do gerenciamento da tabela de protocolos na interface

        # Conexão de sinais e slots para interação com a interface
        self.ui.btn_salvarCadastroProtocolos.clicked.connect(self.cadastrar_protocolo)  # Conexão do botão salvar com a função cadastrar_protocolo
        self.ui.btn_limparCadastroProtocolos.clicked.connect(self.limpar_formulario_protocolo)  # Conexão do botão limpar com a função limpar_formulario_protocolo
        self.ui.btn1_editarProtocolos.clicked.connect(self.editar_protocolo)  # Conexão do botão editar com a função editar_protocolo
        self.ui.btn2_excluirProtocolos.clicked.connect(self.excluir_protocolo)  # Conexão do botão excluir com a função excluir_protocolo
        self.ui.date_protocolosData.setDate(QDate.currentDate())  # Define a data atual no QDateEdit date_protocolosData
        self.ui.btn5_wordProtocolos.clicked.connect(self.salvar_word)
        self.ui.btn4_pdfProtocolos.clicked.connect(self.salvar_pdf)
        self.ui.btn6_whatsappProtocolos.clicked.connect(self.enviar_whatsapp)

        
    def cadastrar_protocolo(self):
        """
        Método para cadastrar um novo protocolo com base nos dados inseridos na interface.
        """
        # Obtendo os dados dos widgets da interface
        data = self.ui.date_protocolosData.date().toString('dd/MM/yyyy')
        hora_inicio = self.ui.date_protocolosInicio.time().toString('HH:mm:ss')
        hora_termino = self.ui.date_protocolosTermino.time().toString('HH:mm:ss')
        cliente = self.ui.cb_protocolosCliente.currentText()
        solicitante = self.ui.cb_protocolosSolicitante.currentText()
        consultor = self.ui.cb_protocolosConsultor.currentText()
        tipo_atendimento = self.ui.cb_protocolosAtendimento.currentText()
        relatorio = self.ui.ed_protocolosDescricao.toPlainText()
        cancelado = 'S' if self.ui.cb_protocolosCancelado.isChecked() else 'N'

        # Verifica se todos os campos obrigatórios foram preenchidos
        if (tipo_atendimento and data and consultor and cliente and solicitante and hora_inicio and hora_termino and relatorio):
            if self.ui.ed_protocolosId.text():
                # Atualiza o protocolo se o ID estiver presente
                id_protocolo = int(self.ui.ed_protocolosId.text())
                protocolo = Protocolo(
                    id=id_protocolo,
                    data=data,
                    cliente=cliente,
                    solicitante=solicitante,
                    consultor=consultor,
                    tipo_atendimento=tipo_atendimento,
                    relatorio=relatorio,
                    hora_inicio=hora_inicio,
                    hora_termino=hora_termino,
                    cancelado=cancelado
                )
                # Atualiza o protocolo no banco de dados
                self.update.atualizar_protocolo(protocolo)
                # Exibe mensagem de sucesso
                self.mensagem.mensagem_informacao(msg_title='Atualização de Protocolo', msg='Protocolo atualizado com sucesso!')
                self.ui.tabela_protocolos.sortItems(0)  # Ordena a tabela pelo ID (coluna 0)
                self.limpar_formulario_protocolo()  # Limpa o formulário
                self.tabela_manager.carregar_protocolos()  # Carrega os protocolos na tabela
            else:
                # Cadastra um novo protocolo se não houver ID
                novo_protocolo = Protocolo(
                    id=None,
                    data=data,
                    cliente=cliente,
                    solicitante=solicitante,
                    consultor=consultor,
                    tipo_atendimento=tipo_atendimento,
                    relatorio=relatorio,
                    hora_inicio=hora_inicio,
                    hora_termino=hora_termino,
                    cancelado=cancelado
                )
                # Insere o novo protocolo no banco de dados
                self.insert.inserir_protocolo(novo_protocolo)
                # Exibe mensagem de sucesso
                self.mensagem.mensagem_informacao(msg_title='Cadastro de Protocolo', msg='Protocolo cadastrado com sucesso!')
                self.ui.tabela_protocolos.sortItems(0)  # Ordena a tabela pelo ID (coluna 0)
                self.limpar_formulario_protocolo()  # Limpa o formulário
                self.tabela_manager.carregar_protocolos()  # Carrega os protocolos na tabela
        else:
            # Exibe mensagem de aviso se algum campo obrigatório não foi preenchido
            self.mensagem.mensagem_aviso(msg_title='O cadastro falhou', msg='Por favor, preencha todos os campos obrigatórios do formulário.')


    def limpar_formulario_protocolo(self):
        """
        Limpa os campos do formulário de protocolos.
        """
        self.ui.ed_protocolosId.clear()
        # Limpa o campo de data para a data atual
        self.ui.date_protocolosData.setDate(QDate.currentDate())

        # Limpa os campos de hora de início e término para os valores padrão
        self.ui.date_protocolosInicio.setTime(QTime(8, 0))  # Define a hora de início para 8:00
        self.ui.date_protocolosTermino.setTime(QTime(17, 0))  # Define a hora de término para 17:00

        # Limpa os textos selecionados nos combobox
        self.ui.cb_protocolosCliente.setCurrentIndex(-1)  # Seleciona o índice -1 para desmarcar todas as opções
        self.ui.cb_protocolosSolicitante.setCurrentIndex(-1)
        self.ui.cb_protocolosConsultor.setCurrentIndex(-1)
        self.ui.cb_protocolosAtendimento.setCurrentIndex(-1)

        # Limpa o texto do QTextEdit
        self.ui.ed_protocolosDescricao.clear()

        # Desmarca o QCheckBox para não estar marcado
        self.ui.cb_protocolosCancelado.setChecked(False)
        self.ui.cb_protocolosCancelado.setEnabled(False)  # Desabilita a edição do checkbox


    def editar_protocolo(self):
        """
        Método para editar um protocolo existente com base na seleção na tabela de protocolos.
        """
        # Verifica se uma linha está selecionada na tabela de protocolos
        if self.ui.tabela_protocolos.selectedItems():
            # Obtém o índice da linha selecionada
            row = self.ui.tabela_protocolos.currentRow()

            # Obtém os dados da linha selecionada na tabela
            id_protocolo = self.ui.tabela_protocolos.item(row, 0).text()
            data = self.ui.tabela_protocolos.item(row, 1).text()
            cliente = self.ui.tabela_protocolos.item(row, 2).text()
            solicitante = self.ui.tabela_protocolos.item(row, 3).text()
            consultor = self.ui.tabela_protocolos.item(row, 4).text()
            tipo_atendimento = self.ui.tabela_protocolos.item(row, 5).text()
            relatorio = self.ui.tabela_protocolos.item(row, 6).text()
            hora_inicio = self.ui.tabela_protocolos.item(row, 7).text()
            hora_termino = self.ui.tabela_protocolos.item(row, 8).text()
            cancelado = self.ui.tabela_protocolos.item(row, 9).text()

            # Preenche os campos na interface com os dados obtidos
            self.ui.ed_protocolosId.setText(str(id_protocolo))
            self.ui.date_protocolosData.setDate(QDate.fromString(data, 'dd/MM/yyyy'))
            self.ui.cb_protocolosCliente.setCurrentText(cliente)
            self.ui.cb_protocolosSolicitante.setCurrentText(solicitante)
            self.ui.cb_protocolosConsultor.setCurrentText(consultor)
            self.ui.cb_protocolosAtendimento.setCurrentText(tipo_atendimento)
            self.ui.ed_protocolosDescricao.setText(relatorio)
            self.ui.date_protocolosInicio.setTime(QTime.fromString(hora_inicio, 'HH:mm:ss'))
            self.ui.date_protocolosTermino.setTime(QTime.fromString(hora_termino, 'HH:mm:ss'))
            self.ui.cb_protocolosCancelado.setChecked(cancelado == 'S')

            self.ui.cb_protocolosCancelado.setEnabled(True)  # Habilita a edição do checkbox de cancelamento
            self.ui.aba_protocolos.setCurrentIndex(1)  # Altera a aba para a de edição
        else:
            # Exibe uma mensagem de aviso se nenhum protocolo estiver selecionado na tabela
            self.mensagem.mensagem_aviso(msg_title='A edição falhou', msg='Por favor, selecione um protocolo na tabela para editar.')


    def excluir_protocolo(self):
        """
        Método para excluir um protocolo existente com base na seleção na tabela de protocolos.
        """
        # Verifica se uma linha está selecionada na tabela de protocolos
        if self.ui.tabela_protocolos.selectedItems():
            # Obtém o índice da linha selecionada
            row = self.ui.tabela_protocolos.currentRow()
            # Obtém o ID do protocolo da linha selecionada e converte para inteiro
            id_protocolo = int(self.ui.tabela_protocolos.item(row, 0).text())

            # Confirma a exclusão do protocolo através do comando de delete
            self.delete.confirmar_exclusao_protocolo(id_protocolo)
            # Ordena a tabela de protocolos pelo ID (coluna 0)
            self.ui.tabela_protocolos.sortItems(0)
            # Limpa o formulário de protocolo após a exclusão
            self.limpar_formulario_protocolo()
            # Carrega novamente os protocolos na tabela após a exclusão
            self.tabela_manager.carregar_protocolos()
        else:
            # Exibe uma mensagem de aviso se nenhum protocolo estiver selecionado na tabela
            self.mensagem.mensagem_aviso(msg_title='A exclusão falhou', msg='Por favor, selecione um protocolo na tabela para excluir.')
    
    
    def salvar_word(self):
        """
        Método para salvar o protocolo selecionado em arquivo Word.
        """
        # Verifica se uma linha está selecionada na tabela de protocolos
        if self.ui.tabela_protocolos.selectedItems():
            # Obter a data atual no formato desejado para o nome do arquivo
            data_atual = datetime.now().strftime("%Y-%m-%d")

            # Nome sugerido para o arquivo
            nome_arquivo = f"Protocolo_{data_atual}.docx"
            # Abrir o diálogo de seleção de pasta e arquivo
            file_path, _ = QFileDialog.getSaveFileName(None, "Salvar Protocolo em Word", nome_arquivo, "Arquivos Word (*.docx)")

            # Verificar se o usuário selecionou um arquivo
            if file_path:
                # Obtém o índice da linha selecionada
                row = self.ui.tabela_protocolos.currentRow()

                # Obtém os dados da linha selecionada na tabela
                id_protocolo = self.ui.tabela_protocolos.item(row, 0).text()
                gerar_relatorio_protocolo_word(id_protocolo, file_path)

                # Exibir mensagem de sucesso após salvar o protocolo em Word
                self.mensagem.mensagem_informacao(msg_title='Salvar Protocolo em Word', msg='O protocolo foi salvo com sucesso em um arquivo Word.')

        else:
            # Exibe uma mensagem de aviso se nenhum protocolo estiver selecionado na tabela
            self.mensagem.mensagem_aviso(msg_title='Erro ao Salvar', msg='Por favor, selecione um protocolo na tabela para salvar em Word.')

        
    def salvar_pdf(self):
        """
        Método para salvar um protocolo em PDF.
        """
        if self.ui.tabela_protocolos.selectedItems():  # Verifica se um protocolo foi selecionado na tabela
            data_atual = datetime.now().strftime("%Y-%m-%d")  # Obtém a data atual no formato YYYY-MM-DD

            # Define o nome do arquivo PDF com base na data atual
            nome_arquivo = f"Protocolo_{data_atual}.pdf"
            current_dir = QDir.currentPath()
            # Permite ao usuário selecionar o local de salvamento e o nome do arquivo
            output_path, _ = QFileDialog.getSaveFileName(None, "Salvar Protocolo em PDF", 
                                                    current_dir + '/' + nome_arquivo, 
                                                    "Arquivos PDF (*.pdf)")

            if output_path:  # Verifica se o usuário selecionou um local de salvamento
                row = self.ui.tabela_protocolos.currentRow()  # Obtém a linha atualmente selecionada na tabela

                id_protocolo = self.ui.tabela_protocolos.item(row, 0).text()  # Obtém o ID do protocolo na tabela
                gerar_relatorio_protocolo_word(id_protocolo, file_path='config/protocolo.docx')  # Gera o relatório do protocolo em formato Word

                # Inicia uma thread para converter o relatório Word em PDF
                self.thread = ConverterPDFThread('config/protocolo.docx', output_path)
                self.thread.finished.connect(self.conversao_concluida)  # Conecta o sinal de conclusão da conversão
                self.thread.start()  # Inicia a thread para realizar a conversão
                self.thread.finished.connect(lambda: self.abrir_pdf(output_path))
        else:
            # Exibe uma mensagem de aviso se nenhum protocolo foi selecionado na tabela
            self.mensagem.mensagem_aviso(msg_title='Erro ao Salvar', msg='Por favor, selecione um protocolo na tabela para salvar em PDF.')


    def conversao_concluida(self):
        """
        Método chamado quando a conversão para PDF é concluída.
        """
        self.mensagem.mensagem_informacao(msg_title='Salvar Protocolo em PDF', msg='O protocolo foi salvo com sucesso em um arquivo PDF.')  # Exibe uma mensagem de informação sobre o sucesso da conversão

    def abrir_pdf(self, file_path):
        try:
            # Usa o comando específico para abrir o arquivo com o visualizador padrão do sistema
            # subprocess.Popen(['xdg-open', file_path])  # No Linux
            # subprocess.Popen(['open', file_path])  # No macOS
            subprocess.Popen(['start', '', file_path], shell=True)  # No Windows
        except Exception as e:
            print(f"Erro ao abrir o arquivo PDF: {e}")
    

    def enviar_whatsapp(self):
        # Verifica se uma linha está selecionada na tabela de protocolos
        if self.ui.tabela_protocolos.selectedItems():
            row = self.ui.tabela_protocolos.currentRow()
            # Obtém o ID do protocolo da linha selecionada e converte para inteiro
            id_protocolo = int(self.ui.tabela_protocolos.item(row, 0).text())
            contato = self.update.buscar_contato_protocolo(id_protocolo)
            caminho_word = 'config/Protocolo.docx'
            caminho_pdf = 'config/Protocolo.pdf'
            gerar_relatorio_protocolo_word(id_protocolo, caminho_word)
            # Inicia uma thread para converter o relatório Word em PDF
            self.thread = ConverterPDFThread(caminho_word, caminho_pdf)
            self.thread.start()  # Inicia a thread para realizar a conversão
            self.thread.finished.connect(lambda: upload_arquivo_e_enviar_whatsapp(contato, caminho_pdf))
        else:
            # Exibe uma mensagem de aviso se nenhum protocolo foi selecionado na tabela
            self.mensagem.mensagem_aviso(msg_title='Erro ao Enviar', msg='Por favor, selecione um protocolo na tabela para enviar via WhatsApp.')


    def salvar_pdf_enviar_whatsapp(self):
        """
        Método para salvar um protocolo em PDF.
        """
        if self.ui.tabela_protocolos.selectedItems():  # Verifica se um protocolo foi selecionado na tabela
            data_atual = datetime.now().strftime("%Y-%m-%d")  # Obtém a data atual no formato YYYY-MM-DD

            # Define o nome do arquivo PDF com base na data atual
            nome_arquivo = f"Protocolo_{data_atual}.pdf"
            current_dir = QDir.currentPath()
            # Permite ao usuário selecionar o local de salvamento e o nome do arquivo
            output_path, _ = QFileDialog.getSaveFileName(None, "Salvar Protocolo em PDF", 
                                                    current_dir + '/' + nome_arquivo, 
                                                    "Arquivos PDF (*.pdf)")

            if output_path:  # Verifica se o usuário selecionou um local de salvamento
                row = self.ui.tabela_protocolos.currentRow()  # Obtém a linha atualmente selecionada na tabela

                id_protocolo = self.ui.tabela_protocolos.item(row, 0).text()  # Obtém o ID do protocolo na tabela
                contato = self.update.buscar_contato_protocolo(id_protocolo)
                caminho_word = 'config/Protocolo.docx'
                gerar_relatorio_protocolo_word(id_protocolo, caminho_word)  # Gera o relatório do protocolo em formato Word
                # Inicia uma thread para converter o relatório Word em PDF
                self.thread = ConverterPDFThread(caminho_word, output_path)
                self.thread.start()  # Inicia a thread para realizar a conversão
                self.thread.finished.connect(lambda: self.abrir_pdf(output_path))
                self.thread.finished.connect(lambda: upload_arquivo_e_enviar_whatsapp(contato, output_path))
        else:
            # Exibe uma mensagem de aviso se nenhum protocolo foi selecionado na tabela
            self.mensagem.mensagem_aviso(msg_title='Erro ao Salvar', msg='Por favor, selecione um protocolo na tabela para salvar em PDF.')
        