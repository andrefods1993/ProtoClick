from app.managers.database_manager import db_manager
from app.controllers.message import Message

class Delete:
    def __init__(self):
        self.message = Message()  # Instância da classe para exibição de mensagens

    def excluir_usuario(self, id_usuario):
        """
        Método para excluir um usuário do banco de dados.

        Args:
            id_usuario (int): ID do usuário a ser excluído.

        Returns:
            bool: True se a exclusão for bem-sucedida, False caso contrário.
        """
        try:
            db_manager.conectar()  # Conecta ao banco de dados
            db_manager.cursor.execute("DELETE FROM Usuario WHERE id = ?", (id_usuario,))
            db_manager.conn.commit()  # Commit das alterações
            print("Usuário excluído com sucesso!")
            return True
        except Exception as e:
            print("Erro ao excluir usuário:", e)
            return False
        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a operação

    def confirmar_exclusao_usuario(self, id_usuario):
        """
        Método para confirmar a exclusão de um usuário.

        Args:
            id_usuario (int): ID do usuário a ser excluído.
        """
        # Exibe um diálogo de confirmação para o usuário
        response = self.message.mensagem_confirmacao(msg_title='Excluir Usuário', msg='Tem certeza que deseja excluir este usuário?')

        if response == "Yes":
            # Se a resposta for "Yes", tenta excluir o usuário
            if self.excluir_usuario(id_usuario):
                self.message.mensagem_informacao(msg_title='Excluído', msg='Usuário excluído com sucesso!')
            else:
                self.message.mensagem_aviso(msg_title='Erro de Exclusão', msg='Erro ao excluir usuário no banco de dados.')
        else:
            # Caso contrário, exibe uma mensagem informando que a exclusão foi cancelada
            self.message.mensagem_informacao(msg_title='Exclusão Cancelada', msg='A exclusão do usuário foi cancelada.')


    def excluir_tipo_atendimento(self, id_tipo_atendimento):
        """
        Método para excluir um tipo de atendimento do banco de dados.

        Args:
            id_tipo_atendimento (int): ID do tipo de atendimento a ser excluído.

        Returns:
            bool: True se a exclusão for bem-sucedida, False caso contrário.
        """
        try:
            db_manager.conectar()  # Conecta ao banco de dados
            db_manager.cursor.execute("DELETE FROM TipoAtendimento WHERE id = ?", (id_tipo_atendimento,))
            db_manager.conn.commit()  # Commit das alterações
            print("Tipo atendimento excluído com sucesso!")
            return True
        except Exception as e:
            print("Erro ao excluir tipo atendimento:", e)
            return False
        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a operação

    def confirmar_exclusao_tipo_atendimento(self, id_tipo_atendimento):
        """
        Método para confirmar a exclusão de um tipo de atendimento.

        Args:
            id_tipo_atendimento (int): ID do tipo de Atendimento a ser excluído.
        """
        # Exibe um diálogo de confirmação para o tipo de atendimento
        response = self.message.mensagem_confirmacao(msg_title='Excluir Tipo de Atendimento', msg='Tem certeza que deseja excluir este tipo de atendimento?')

        if response == "Yes":
            # Se a resposta for "Yes", tenta excluir o tipo de atendimento
            if self.excluir_tipo_atendimento(id_tipo_atendimento):
                self.message.mensagem_informacao(msg_title='Excluído', msg='Tipo de Atendimento excluído com sucesso!')
            else:
                self.message.mensagem_aviso(msg_title='Erro de Exclusão', msg='Erro ao excluir tipo de atendimento no banco de dados.')
        else:
            # Caso contrário, exibe uma mensagem informando que a exclusão foi cancelada
            self.message.mensagem_informacao(msg_title='Exclusão Cancelada', msg='A exclusão do tipo de atendimento foi cancelada.')


    def excluir_aviso(self, id_aviso):
        """
        Método para excluir um aviso do banco de dados.

        Args:
            id_aviso (int): ID do aviso a ser excluído.

        Returns:
            bool: True se a exclusão for bem-sucedida, False caso contrário.
        """
        try:
            db_manager.conectar()  # Conecta ao banco de dados
            db_manager.cursor.execute("DELETE FROM Aviso WHERE id = ?", (id_aviso,))
            db_manager.conn.commit()  # Commit das alterações
            print("Aviso excluído com sucesso!")
            return True
        except Exception as e:
            print("Erro ao excluir o aviso:", e)
            return False
        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a operação

    def confirmar_exclusao_aviso(self, id_aviso):
        """
        Método para confirmar a exclusão de um aviso.

        Args:
            id_aviso (int): ID do aviso a ser excluído.
        """
        # Exibe um diálogo de confirmação para o aviso
        response = self.message.mensagem_confirmacao(msg_title='Excluir Aviso', msg='Tem certeza que deseja excluir este aviso?')

        if response == "Yes":
            # Se a resposta for "Yes", tenta excluir o aviso
            if self.excluir_aviso(id_aviso):
                self.message.mensagem_informacao(msg_title='Excluído', msg='Aviso excluído com sucesso!')
            else:
                self.message.mensagem_aviso(msg_title='Erro de Exclusão', msg='Erro ao excluir o aviso no banco de dados.')
        else:
            # Caso contrário, exibe uma mensagem informando que a exclusão foi cancelada
            self.message.mensagem_informacao(msg_title='Exclusão Cancelada', msg='A exclusão do aviso foi cancelada.')


    def excluir_cliente(self, id_cliente):
        """
        Método para excluir um cliente do banco de dados.

        Args:
            id_cliente (int): ID do cliente a ser excluído.

        Returns:
            bool: True se a exclusão for bem-sucedida, False caso contrário.
        """
        try:
            db_manager.conectar()  # Conecta ao banco de dados
            # Deleta o registro do endereço associado ao cliente
            db_manager.cursor.execute(
                        """
                DELETE FROM EnderecoCliente
                WHERE cliente_id = ?
                """,
                (id_cliente,)
            )

            # Deleta o registro do solicitante associado ao cliente
            db_manager.cursor.execute(
                """
                DELETE FROM SolicitanteCliente
                WHERE cliente_id = ?
                """,
                (id_cliente,)
            )

            # Deleta o cliente
            db_manager.cursor.execute(
                """
                DELETE FROM Cliente
                WHERE id = ?
                """,
                (id_cliente,)
            )
            db_manager.conn.commit()  # Commit das alterações
            print("Cliente excluído com sucesso!")
            return True
        except Exception as e:
            print("Erro ao excluir o cliente:", e)
            return False
        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a operação

    def confirmar_exclusao_cliente(self, id_cliente):
        """
        Método para confirmar a exclusão de um cliente.

        Args:
            id_cliente (int): ID do cliente a ser excluído.
        """
        # Exibe um diálogo de confirmação para o usuário
        response = self.message.mensagem_confirmacao(msg_title='Excluir Cliente', msg='Tem certeza que deseja excluir este cliente?')

        if response == "Yes":
            # Se a resposta for "Yes", tenta excluir o cliente
            if self.excluir_cliente(id_cliente):
                self.message.mensagem_informacao(msg_title='Excluído', msg='Cliente excluído com sucesso!')
            else:
                self.message.mensagem_aviso(msg_title='Erro de Exclusão', msg='Erro ao excluir o cliente no banco de dados.')
        else:
            # Caso contrário, exibe uma mensagem informando que a exclusão foi cancelada
            self.message.mensagem_informacao(msg_title='Exclusão Cancelada', msg='A exclusão do cliente foi cancelada.')


    def excluir_empresa(self, id_empresa):
        """
        Método para excluir uma empresa do banco de dados.

        Args:
            id_empresa (int): ID da empresa a ser excluído.

        Returns:
            bool: True se a exclusão for bem-sucedida, False caso contrário.
        """
        try:
            db_manager.conectar()  # Conecta ao banco de dados
            # Deleta a empresa
            db_manager.cursor.execute(
                """
                DELETE FROM Empresa
                WHERE id = ?
                """,
                (id_empresa,)
            )
            db_manager.conn.commit()  # Commit das alterações
            print("Empresa excluído com sucesso!")
            return True
        except Exception as e:
            print("Erro ao excluir a empresa:", e)
            return False
        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a operação

    def confirmar_exclusao_empresa(self, id_empresa):
        """
        Método para confirmar a exclusão de uma empresa.

        Args:
            id_empresa (int): ID da empresa a ser excluído.
        """
        # Exibe um diálogo de confirmação para o usuário
        response = self.message.mensagem_confirmacao(msg_title='Excluir Empresa', msg='Tem certeza que deseja excluir esta empresa?')

        if response == "Yes":
            # Se a resposta for "Yes", tenta excluir a empresa
            if self.excluir_empresa(id_empresa):
                self.message.mensagem_informacao(msg_title='Excluído', msg='Empresa excluída com sucesso!')
                return response
            else:
                self.message.mensagem_aviso(msg_title='Erro de Exclusão', msg='Erro ao excluir a empresa no banco de dados.')
        else:
            # Caso contrário, exibe uma mensagem informando que a exclusão foi cancelada
            self.message.mensagem_informacao(msg_title='Exclusão Cancelada', msg='A exclusão da empresa foi cancelada.')

    
    def excluir_logo(self, id_empresa):
        """
        Método para excluir uma logo do banco de dados.

        Args:
            id_empresa (int): ID da empresa da logo a ser excluída.

        Returns:
            bool: True se a exclusão for bem-sucedida, False caso contrário.
        """
        try:
            db_manager.conectar()  # Conecta ao banco de dados
            # Deleta a logo
            db_manager.cursor.execute(
                """
                UPDATE Empresa SET logo = NULL WHERE id = ?
                """,
                (id_empresa,)
            )
            db_manager.conn.commit()  # Commit das alterações
            print("Logo excluída com sucesso!")
            return True
        except Exception as e:
            print("Erro ao excluir a logo:", e)
            return False
        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a operação

    def confirmar_exclusao_logo(self, id_empresa):
        """
        Método para confirmar a exclusão de uma logo.

        Args:
            id_empresa (int): ID da empresa com a logo a ser excluído.
        """
        # Exibe um diálogo de confirmação para o usuário
        response = self.message.mensagem_confirmacao(msg_title='Excluir Logo', msg='Tem certeza que deseja excluir esta logo?')

        if response == "Yes":
            # Se a resposta for "Yes", tenta excluir a logo
            if self.excluir_logo(id_empresa):
                self.message.mensagem_informacao(msg_title='Excluído', msg='Logo excluída com sucesso!')
                return response
            else:
                self.message.mensagem_aviso(msg_title='Erro de Exclusão', msg='Erro ao excluir a logo no banco de dados.')
        else:
            # Caso contrário, exibe uma mensagem informando que a exclusão foi cancelada
            self.message.mensagem_informacao(msg_title='Exclusão Cancelada', msg='A exclusão da logo foi cancelada.')


    def excluir_protocolo(self, id_protocolo):
        """
        Método para excluir um protocolo do banco de dados.

        Args:
            id_protocolo (int): ID do protocolo a ser excluído.

        Returns:
            bool: True se a exclusão for bem-sucedida, False caso contrário.
        """
        try:
            db_manager.conectar()  # Conecta ao banco de dados
            db_manager.cursor.execute("DELETE FROM ProtocoloAtendimento WHERE id = ?", (id_protocolo,))
            db_manager.conn.commit()  # Commit das alterações
            print("Protocolo excluído com sucesso!")
            return True
        except Exception as e:
            print("Erro ao excluir o protocolo:", e)
            return False
        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a operação

    def confirmar_exclusao_protocolo(self, id_protocolo):
        """
        Método para confirmar a exclusão de um protocolo.

        Args:
            id_protocolo (int): ID do protocolo a ser excluído.
        """
        # Exibe um diálogo de confirmação para o usuário
        response = self.message.mensagem_confirmacao(msg_title='Excluir Protocolo', msg='Tem certeza que deseja excluir este protocolo?')

        if response == "Yes":
            # Se a resposta for "Yes", tenta excluir o protocolo
            if self.excluir_protocolo(id_protocolo):
                self.message.mensagem_informacao(msg_title='Excluído', msg='Protocolo excluído com sucesso!')
            else:
                self.message.mensagem_aviso(msg_title='Erro de Exclusão', msg='Erro ao excluir o protocolo no banco de dados.')
        else:
            # Caso contrário, exibe uma mensagem informando que a exclusão foi cancelada
            self.message.mensagem_informacao(msg_title='Exclusão Cancelada', msg='A exclusão do protocolo foi cancelada.')
