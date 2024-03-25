import sqlite3
from app.managers.database_manager import db_manager

class Insert:
    
    def inserir_usuario(self, usuario):
        """
        Insere um novo usuário no banco de dados.

        Args:
            usuario: Objeto Usuario com os dados do novo usuário.

        Returns:
            bool: True se o cadastro for bem-sucedido, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para inserir um novo usuário
            db_manager.cursor.execute(
                "INSERT INTO Usuario (nome, contato, email, funcao) VALUES (?, ?, ?, ?)",
                (usuario.nome, usuario.contato, usuario.email, usuario.funcao)
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Usuário cadastrado com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao cadastrar usuário:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def inserir_tipo_atendimento(self, tipo_atendimento):
        """
        Insere um novo tipo de atendimento no banco de dados.

        Args:
            tipo_atendimento: Objeto TipoAtendimento com os dados do novo tipo_atendimento.

        Returns:
            bool: True se o cadastro for bem-sucedido, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para inserir um novo tipo de atendimento
            db_manager.cursor.execute(
                "INSERT INTO TipoAtendimento (descricao) VALUES (?)",
                (tipo_atendimento.descricao,)
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Tipo Atendimento cadastrado com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao cadastrar tipo de atendimento:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def inserir_aviso(self, aviso):
        """
        Insere um novo aviso no banco de dados.

        Args:
            aviso: Objeto Aviso com os dados do novo aviso.

        Returns:
            bool: True se o cadastro for bem-sucedido, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para inserir um novo aviso
            db_manager.cursor.execute(
                "INSERT INTO Aviso (descricao, mensagem) VALUES (?, ?)",
                (aviso.descricao, aviso.mensagem)
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Aviso cadastrado com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao cadastrar o aviso:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def inserir_cliente(self, cliente):
        """
        Insere um novo cliente no banco de dados.

        Args:
            cliente: Objeto Cliente com os dados do novo cliente.

        Returns:
            bool: True se o cadastro for bem-sucedido, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para inserir um novo cliente
            db_manager.cursor.execute(
                """
                INSERT INTO Cliente (razao_social, cpf_cnpj, natureza_social, contato, email, desativado)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    cliente.razao_social, cliente.cpf_cnpj, cliente.natureza_social, cliente.contato,
                    cliente.email, cliente.desativado
                )
            )
            # Obtém o ID do cliente recém-inserido
            id_cliente = db_manager.cursor.lastrowid

            # Insere os dados em SolicitanteCliente
            db_manager.cursor.execute(
                """
                INSERT INTO SolicitanteCliente (cliente_id, nome)
                VALUES (?, ?)
                """,
                (id_cliente, cliente.solicitante)
            )

            # Insere os dados em EnderecoCliente
            db_manager.cursor.execute(
                """
                INSERT INTO EnderecoCliente (cliente_id, cep, logradouro, numero, bairro, cidade_id, uf_id, referencia)
                VALUES (?, ?, ?, ?, ?, (SELECT id FROM Cidade WHERE descricao = ?),
                                    (SELECT id FROM UF WHERE uf = ?), ?)
                """,
                (
                    id_cliente, cliente.cep, cliente.logradouro, cliente.numero, cliente.bairro,
                    cliente.cidade, cliente.uf, cliente.referencia
                )
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Cliente cadastrado com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao cadastrar o cliente:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def inserir_empresa(self, empresa):
        """
        Insere um nova empresa no banco de dados.

        Args:
            empresa: Objeto Empresa com os dados da nova empresa.

        Returns:
            bool: True se o cadastro for bem-sucedido, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            
            # Executa a query para inserir um novo cliente
            db_manager.cursor.execute(
                """
                INSERT INTO Empresa (razao_social, natureza_social, cpf_cnpj, contato, email,
                                    endereco_cep, endereco_logradouro, endereco_numero,
                                    endereco_bairro, endereco_referencia, cidade_id, uf_id)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, (SELECT id FROM Cidade WHERE descricao = ?),
                        (SELECT id FROM UF WHERE uf = ?))
                """,
                (
                    empresa.razao_social, empresa.natureza_social, empresa.cpf_cnpj, empresa.contato,
                    empresa.email, empresa.endereco_cep, empresa.endereco_logradouro,
                    empresa.endereco_numero, empresa.endereco_bairro, empresa.endereco_referencia,
                    empresa.cidade, empresa.uf
                )
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Empresa salva com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao cadastrar a empresa:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()


    def inserir_protocolo(self, protocolo):
        """
        Insere um novo protocolo no banco de dados.

        Args:
            protocolo: Objeto Protocolo com os dados do novo protocolo.

        Returns:
            bool: True se o cadastro for bem-sucedido, False caso contrário.
        """
        try:
            # Conecta ao banco de dados
            db_manager.conectar()
            # Executa a query para inserir um novo protocolo
            db_manager.cursor.execute(
                """
                INSERT INTO ProtocoloAtendimento (data, cliente_id, solicitante_cliente_id, usuario_id,
                                                tipo_atendimento_id, relatorio, hora_inicio,
                                                hora_termino, cancelado)
                VALUES (?, (SELECT id FROM Cliente WHERE razao_social = ?),
                        (SELECT id FROM SolicitanteCliente WHERE nome = ? and cliente_id = (SELECT id FROM Cliente WHERE razao_social = ?)),
                        (SELECT id FROM Usuario WHERE nome = ?),
                        (SELECT id FROM TipoAtendimento WHERE descricao = ?), ?, ?, ?, ?)
                """,
                (
                    protocolo.data, protocolo.cliente, protocolo.solicitante, protocolo.cliente,
                    protocolo.consultor, protocolo.tipo_atendimento, protocolo.relatorio, protocolo.hora_inicio,
                    protocolo.hora_termino, protocolo.cancelado
                )
            )
            # Confirma a transação
            db_manager.conn.commit()
            # Exibe mensagem de sucesso
            print("Protocolo cadastrado com sucesso!")
            return True
        except sqlite3.Error as e:
            # Exibe mensagem de erro caso ocorra uma exceção
            print("Erro ao cadastrar o protocolo:", e)
            return False
        finally:
            # Desconecta do banco de dados após a execução
            db_manager.desconectar()
