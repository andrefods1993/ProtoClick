import sqlite3
from app.managers.database_manager import db_manager

class Update:
    
    def atualizar_usuario(self, usuario):
        """
        Atualiza um usuário no banco de dados.

        Args:
            usuario: Objeto Usuario com os dados atualizados.

        Returns:
            bool: True se a atualização for bem-sucedida, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para atualizar o usuário
            db_manager.cursor.execute(
                "UPDATE Usuario SET nome = ?, contato = ?, email = ?, funcao = ?, desativado = ? WHERE id = ?",
                (usuario.nome, usuario.contato, usuario.email, usuario.funcao, usuario.desativado, usuario.id)
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Usuário atualizado com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao atualizar usuário:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def atualizar_tipo_atendimento(self, tipo_atendimento):
        """
        Atualiza um tipo de atendimento no banco de dados.

        Args:
            tipo_atendimento: Objeto TipoAtendimento com os dados atualizados.

        Returns:
            bool: True se a atualização for bem-sucedida, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para atualizar o tipo de atendimento
            db_manager.cursor.execute(
                "UPDATE TipoAtendimento SET descricao = ?, desativado = ? WHERE id = ?",
                (tipo_atendimento.descricao, tipo_atendimento.desativado, tipo_atendimento.id)
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Tipo de Atendimento atualizado com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao atualizar o tipo de atendimento:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def atualizar_aviso(self, aviso):
        """
        Atualiza um aviso no banco de dados.

        Args:
            aviso: Objeto Aviso com os dados atualizados.

        Returns:
            bool: True se a atualização for bem-sucedida, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para atualizar o aviso
            db_manager.cursor.execute(
                "UPDATE Aviso SET descricao = ?, mensagem = ?, desativado = ? WHERE id = ?",
                (aviso.descricao, aviso.mensagem, aviso.desativado, aviso.id)
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Aviso atualizado com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao atualizar o aviso:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def atualizar_cliente(self, cliente):
        """
        Atualiza um cliente no banco de dados.

        Args:
            cliente: Objeto Cliente com os dados atualizados.

        Returns:
            bool: True se a atualização for bem-sucedida, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para atualizar o usuário
            db_manager.cursor.execute(
                """
                UPDATE Cliente
                SET razao_social = ?, cpf_cnpj = ?, natureza_social = ?, contato = ?, email = ?,
                    desativado = ?
                WHERE id = ?
                """,
                (
                    cliente.razao_social, cliente.cpf_cnpj, cliente.natureza_social, cliente.contato,
                    cliente.email, cliente.desativado, cliente.id
                )
            )

            # Atualiza os dados em SolicitanteCliente
            db_manager.cursor.execute(
                """
                UPDATE SolicitanteCliente
                SET nome = ?
                WHERE cliente_id = ?
                """,
                (cliente.solicitante, cliente.id)
            )

            # Atualiza os dados em EnderecoCliente
            db_manager.cursor.execute(
                """
                UPDATE EnderecoCliente
                SET cep = ?, logradouro = ?, numero = ?, bairro = ?, cidade_id = (SELECT id FROM Cidade WHERE descricao = ?),
                    uf_id = (SELECT id FROM UF WHERE uf = ?), referencia = ?
                WHERE cliente_id = ?
                """,
                (
                    cliente.cep, cliente.logradouro, cliente.numero, cliente.bairro, cliente.cidade,
                    cliente.uf, cliente.referencia, cliente.id
                )
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Cliente atualizado com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao atualizar o cliente:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def atualizar_empresa(self, empresa):
        """
        Atualiza uma empresa no banco de dados.

        Args:
            empresa: Objeto Empresa com os dados atualizados.

        Returns:
            bool: True se a atualização for bem-sucedida, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para atualizar a empresa
            db_manager.cursor.execute(
                """
                UPDATE Empresa
                SET razao_social = ?, natureza_social = ?, cpf_cnpj = ?, contato = ?, email = ?,
                    endereco_cep = ?, endereco_logradouro = ?, endereco_numero = ?, 
                    endereco_bairro = ?, endereco_referencia = ?, cidade_id = (SELECT id FROM Cidade WHERE descricao = ?),
                    uf_id = (SELECT id FROM UF WHERE uf = ?)
                WHERE id = ?
                """,
                (
                    empresa.razao_social, empresa.natureza_social, empresa.cpf_cnpj, empresa.contato,
                    empresa.email, empresa.endereco_cep, empresa.endereco_logradouro,
                    empresa.endereco_numero, empresa.endereco_bairro, empresa.endereco_referencia,
                    empresa.cidade, empresa.uf, empresa.id
                )
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Empresa atualizado com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao atualizar a empresa:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def atualizar_logo(self, logo, id_empresa):
        """
        Insere uma logo no banco de dados na empresa cadastrada.

        Args:
            id_empresa: ID da empresa que vai atualizar a logo.

        Returns:
            bool: True se o cadastro for bem-sucedido, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para inserir um novo cliente
            db_manager.cursor.execute(
               """
                    UPDATE Empresa
                    SET logo = ?
                    WHERE id = ?
                """,
                (
                    logo, id_empresa
                )
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Logo atualizada com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao atualizar logo:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def atualizar_protocolo(self, protocolo):
        """
        Atualiza um protocolo no banco de dados.

        Args:
            protocolo: Objeto Protocolo com os dados atualizados.

        Returns:
            bool: True se a atualização for bem-sucedida, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para atualizar o protocolo
            db_manager.cursor.execute(
                """
                UPDATE ProtocoloAtendimento
                SET 
                    data = ?,
                    cliente_id = (SELECT id FROM Cliente WHERE razao_social = ?),
                    solicitante_cliente_id = (SELECT id FROM SolicitanteCliente WHERE nome = ? and cliente_id = (SELECT id FROM Cliente WHERE razao_social = ?)),
                    usuario_id = (SELECT id FROM Usuario WHERE nome = ?),
                    tipo_atendimento_id = (SELECT id FROM TipoAtendimento WHERE descricao = ?),
                    relatorio = ?,
                    hora_inicio = ?,
                    hora_termino = ?,
                    cancelado = ?
                WHERE id = ? """,
                (
                    protocolo.data, protocolo.cliente, protocolo.solicitante, protocolo.cliente, protocolo.consultor,
                    protocolo.tipo_atendimento, protocolo.relatorio, protocolo.hora_inicio,
                    protocolo.hora_termino, protocolo.cancelado, protocolo.id
                )
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Protocolo atualizado com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao atualizar o protocolo:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def buscar_contato_protocolo(self, id_protocolo):
        contato = []
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para atualizar o protocolo
            db_manager.cursor.execute(
                """
                SELECT
                    C.contato
                FROM ProtocoloAtendimento P
                LEFT JOIN Cliente C ON P.cliente_id = C.id
                WHERE P.id = ? """,
                (id_protocolo,)
            )
            row = db_manager.cursor.fetchone()
            if row:
                # Extrai apenas os números do contato
                contato_str = ''.join(filter(str.isdigit, row[0]))
                contato.append(contato_str)

        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao encontrar o contato:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()
        return contato