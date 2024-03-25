import sqlite3

from app.managers.database_manager import db_manager
from app.models.usuario import Usuario
from app.models.cliente import Cliente
from app.models.tipo_atendimento import TipoAtendimento
from app.models.aviso import Aviso
from app.models.cidade import Cidade
from app.models.uf import UF
from app.models.empresa import Empresa
from app.models.solicitante import Solicitante
from app.models.protocolo import Protocolo

class DataManager:

    def buscar_usuarios(self):
        # Inicializa uma lista vazia para armazenar os usuários encontrados
        usuarios = []

        # Conecta ao banco de dados
        db_manager.conectar()
        
        try:
            # Executa uma consulta SQL para buscar todos os usuários na tabela Usuario
            db_manager.cursor.execute("SELECT * FROM Usuario")
            rows = db_manager.cursor.fetchall()  # Recupera todas as linhas resultantes da consulta

            # Itera sobre as linhas recuperadas para criar objetos Usuario e adicioná-los à lista de usuários
            for row in rows:
                usuario = Usuario(
                    id=row[0],
                    nome=row[1],
                    contato=row[2],
                    email=row[3],
                    funcao=row[4],
                    desativado=row[5]
                )
                usuarios.append(usuario)

        except sqlite3.Error as e:
            print("Erro ao buscar usuários no banco de dados:", e)  # Imprime mensagem de erro em caso de falha na busca

        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a execução da consulta

        return usuarios  # Retorna a lista de usuários encontrados


    def buscar_clientes(self):
        # Inicializa uma lista vazia para armazenar os clientes encontrados
        clientes = []

        # Conecta ao banco de dados
        db_manager.conectar()
        
        try:
            # Executa uma consulta SQL para buscar todos os clientes na tabela cliente
            db_manager.cursor.execute(
                """
                SELECT C.id, C.razao_social, C.cpf_cnpj,
                    C.natureza_social, C.contato, C.email, SC.nome,
                    EC.cep, EC.logradouro, EC.numero, EC.bairro,
                    CID.descricao AS cidade, UF.uf AS uf,
                    EC.referencia, C.desativado
                FROM Cliente C
                LEFT JOIN SolicitanteCliente SC ON C.id = SC.cliente_id
                LEFT JOIN EnderecoCliente EC ON C.id = EC.cliente_id
                LEFT JOIN Cidade CID ON EC.cidade_id = CID.id
                LEFT JOIN UF UF ON EC.uf_id = UF.id
                """
            )
            rows = db_manager.cursor.fetchall()  # Recupera todas as linhas resultantes da consulta

            # Itera sobre as linhas recuperadas para criar objetos Cliente e adicioná-los à lista de clientes
            for row in rows:
                cliente = Cliente(
                    id=row[0],
                    razao_social=row[1],
                    cpf_cnpj=row[2],
                    natureza_social=row[3],
                    contato=row[4],
                    email=row[5],
                    solicitante=row[6],
                    cep=row[7],
                    logradouro=row[8],
                    numero=row[9],
                    bairro=row[10],
                    cidade=row[11],
                    uf=row[12],
                    referencia=row[13],
                    desativado=row[14]
                )
                clientes.append(cliente)

        except sqlite3.Error as e:
            print("Erro ao buscar clientes no banco de dados:", e)  # Imprime mensagem de erro em caso de falha na busca

        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a execução da consulta

        return clientes  # Retorna a lista de clientes encontrados
    

    def buscar_tipos_atendimento(self):
        # Inicializa uma lista vazia para armazenar os tipos de atendimento encontrados
        tipos_atendimento = []

        # Conecta ao banco de dados
        db_manager.conectar()
        
        try:
            # Executa uma consulta SQL para buscar todos os tipos de atendimento na tabela TipoAtendimento 
            db_manager.cursor.execute("SELECT * FROM TipoAtendimento")
            rows = db_manager.cursor.fetchall()  # Recupera todas as linhas resultantes da consulta

            # Itera sobre as linhas recuperadas para criar objetos TipoAtendimento e adicioná-los à lista de usuários
            for row in rows:
                tipo_atendimento = TipoAtendimento(
                    id=row[0],
                    descricao=row[1],
                    desativado=row[2]
                )
                tipos_atendimento.append(tipo_atendimento)

        except sqlite3.Error as e:
            print("Erro ao buscar os tipos de atendimento no banco de dados:", e)  # Imprime mensagem de erro em caso de falha na busca

        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a execução da consulta

        return tipos_atendimento  # Retorna a lista de tipos de atendimento encontrados
    

    def buscar_avisos(self):
        # Inicializa uma lista vazia para armazenar os avisos encontrados
        avisos = []

        # Conecta ao banco de dados
        db_manager.conectar()
        
        try:
            # Executa uma consulta SQL para buscar todos os avisos na tabela Aviso
            db_manager.cursor.execute("SELECT * FROM Aviso")
            rows = db_manager.cursor.fetchall()  # Recupera todas as linhas resultantes da consulta

            # Itera sobre as linhas recuperadas para criar objetos Aviso e adicioná-los à lista de avisos
            for row in rows:
                aviso = Aviso(
                    id=row[0],
                    descricao=row[1],
                    mensagem=row[2],
                    desativado=row[3]
                )
                avisos.append(aviso)

        except sqlite3.Error as e:
            print("Erro ao buscar os avisos no banco de dados:", e)  # Imprime mensagem de erro em caso de falha na busca

        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a execução da consulta

        return avisos  # Retorna a lista de avisos encontrados
    

    def buscar_cidades(self):
        # Inicializa uma lista vazia para armazenar as cidades encontradas
        cidades = []

        # Conecta ao banco de dados
        db_manager.conectar()
        
        try:
            # Executa uma consulta SQL para buscar todos as cidades na tabela Cidade
            db_manager.cursor.execute("SELECT * FROM Cidade")
            rows = db_manager.cursor.fetchall()  # Recupera todas as linhas resultantes da consulta

            # Itera sobre as linhas recuperadas para criar objetos Cidade e adicioná-los à lista de cidades
            for row in rows:
                cidade = Cidade(
                    id=row[0],
                    descricao=row[1],
                    uf_id=row[2]
                )
                cidades.append(cidade)

        except sqlite3.Error as e:
            print("Erro ao buscar as cidades no banco de dados:", e)  # Imprime mensagem de erro em caso de falha na busca

        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a execução da consulta

        return cidades  # Retorna a lista de cidades encontrados
    

    def buscar_uf(self):
        # Inicializa uma lista vazia para armazenar as UF's encontradas
        ufs = []

        # Conecta ao banco de dados
        db_manager.conectar()
        
        try:
            # Executa uma consulta SQL para buscar todos as UF's na tabela UF
            db_manager.cursor.execute("SELECT * FROM UF")
            rows = db_manager.cursor.fetchall()  # Recupera todas as linhas resultantes da consulta

            # Itera sobre as linhas recuperadas para criar objetos UF e adicioná-los à lista de UF's
            for row in rows:
                uf = UF(
                    id=row[0],
                    descricao=row[1],
                    uf=row[2]
                )
                ufs.append(uf)

        except sqlite3.Error as e:
            print("Erro ao buscar as UF's no banco de dados:", e)  # Imprime mensagem de erro em caso de falha na busca

        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a execução da consulta

        return ufs  # Retorna a lista de UF's encontradas
    

    def buscar_cidades_por_uf(self, uf_id):
        cidades = []  # Inicializa uma lista vazia para armazenar as cidades encontradas

        db_manager.conectar()  # Conecta ao banco de dados usando o gerenciador db_manager

        try:
            # Executa a consulta SQL para obter as cidades com base no ID da UF
            db_manager.cursor.execute("SELECT * FROM Cidade WHERE UF_id = ?", (uf_id,))
            rows = db_manager.cursor.fetchall()  # Obtém todas as linhas resultantes da consulta

            # Itera sobre as linhas retornadas e cria objetos Cidade para cada uma delas
            for row in rows:
                cidade = Cidade(row[0], row[1], row[2])  # Supondo que Cidade seja uma classe com atributos correspondentes
                cidades.append(cidade)  # Adiciona a cidade à lista de cidades

        except sqlite3.Error as e:
            print("Erro ao buscar cidades por UF no banco de dados:", e)

        finally:
            db_manager.desconectar()  # Garante que a conexão com o banco de dados seja encerrada

        return cidades  # Retorna a lista de cidades encontradas


    def buscar_empresa(self):
        # Inicializa uma lista vazia para armazenar os usuários encontrados
        empresas = []

        # Conecta ao banco de dados
        db_manager.conectar()
        
        try:
            # Executa uma consulta SQL para buscar todos os usuários na tabela Usuario
            db_manager.cursor.execute(
                """
                SELECT
                    E.id,
                    E.razao_social,
                    E.natureza_social,
                    E.cpf_cnpj, contato,
                    E.email,
                    E.logo,
                    E.endereco_cep,
                    E.endereco_logradouro,
                    E.endereco_numero,
                    E.endereco_bairro,
                    E.endereco_referencia,
                    CD.descricao,
                    UF.uf
                FROM Empresa E
                LEFT JOIN Cidade CD ON E.cidade_id = CD.id
                LEFT JOIN UF UF ON E.uf_id = UF.id
                """
            )
            rows = db_manager.cursor.fetchall()  # Recupera todas as linhas resultantes da consulta

            # Itera sobre as linhas recuperadas para criar objetos Empresa e adicioná-los à lista de empresa
            for row in rows:
                empresa = Empresa(
                    id=row[0],
                    razao_social=row[1],
                    natureza_social=row[2],
                    cpf_cnpj=row[3],
                    contato=row[4],
                    email=row[5],
                    logo=row[6],
                    endereco_cep=row[7],
                    endereco_logradouro=row[8],
                    endereco_numero=row[9],
                    endereco_bairro=row[10],
                    endereco_referencia=row[11],
                    cidade=row[12],
                    uf=row[13]
                )
                empresas.append(empresa)

        except sqlite3.Error as e:
            print("Erro ao buscar a empresa no banco de dados:", e)  # Imprime mensagem de erro em caso de falha na busca

        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a execução da consulta

        return empresas  # Retorna a lista de empresa encontrados


    def buscar_solicitante_por_cliente(self, cliente_id):
        solicitantes = []  # Inicializa uma lista vazia para armazenar solicitantes encontrados

        db_manager.conectar()  # Conecta ao banco de dados usando o gerenciador db_manager

        try:
            # Executa a consulta SQL para obter solicitantes com base no ID do cliente
            db_manager.cursor.execute("SELECT * FROM SolicitanteCliente WHERE cliente_id = ?", (cliente_id,))
            rows = db_manager.cursor.fetchall()  # Obtém todas as linhas resultantes da consulta

            # Itera sobre as linhas retornadas e cria objetos Solicitante para cada uma delas
            for row in rows:
                solicitante = Solicitante(row[0], row[1], row[2])  # Supondo que Solicitante seja uma classe com atributos correspondentes
                solicitantes.append(solicitante)  # Adiciona o solicitante à lista de solicitantes

        except sqlite3.Error as e:
            print("Erro ao buscar solicitantes por clientes no banco de dados:", e)

        finally:
            db_manager.desconectar()  # Garante que a conexão com o banco de dados seja encerrada

        return solicitantes  # Retorna a lista de solicitantes encontrados
    

    def buscar_protocolos(self):
        # Inicializa uma lista vazia para armazenar os protocolos encontrados
        protocolos = []

        # Conecta ao banco de dados
        db_manager.conectar()
        
        try:
            # Executa uma consulta SQL para buscar todos os protocolos na tabela ProtocoloAtendimento
            db_manager.cursor.execute(
                """
                SELECT
                    PA.id,
                    PA.data,
                    CL.razao_social,
                    SC.nome,
                    US.nome,
                    TP.descricao,
                    PA.relatorio,
                    PA.hora_inicio,
                    PA.hora_termino,
                    PA.cancelado
                FROM ProtocoloAtendimento PA
                LEFT JOIN TipoAtendimento TP ON PA.tipo_atendimento_id = TP.id
                LEFT JOIN Usuario US ON PA.usuario_id = US.id
                LEFT JOIN Cliente CL ON PA.cliente_id = CL.id
                LEFT JOIN SolicitanteCliente SC ON PA.solicitante_cliente_id = SC.id
                """
            )
            rows = db_manager.cursor.fetchall()  # Recupera todas as linhas resultantes da consulta

            # Itera sobre as linhas recuperadas para criar objetos Protocolo e adicioná-los à lista de protocolos
            for row in rows:
                protocolo = Protocolo(
                    id=row[0],
                    data=row[1],
                    cliente=row[2],
                    solicitante=row[3],
                    consultor=row[4],
                    tipo_atendimento=row[5],
                    relatorio=row[6],
                    hora_inicio=row[7],
                    hora_termino=row[8],
                    cancelado=row[9]
                )
                protocolos.append(protocolo)

        except sqlite3.Error as e:
            print("Erro ao buscar os protocolos no banco de dados:", e)  # Imprime mensagem de erro em caso de falha na busca

        finally:
            db_manager.desconectar()  # Desconecta do banco de dados após a execução da consulta

        return protocolos  # Retorna a lista de protocolos encontrados
