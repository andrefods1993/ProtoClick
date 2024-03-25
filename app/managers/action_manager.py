from PySide6.QtWidgets import QComboBox

def conectar_comboboxes(combo_uf: QComboBox, combo_cidade: QComboBox, combo_manager):
    """
    Conecta um ComboBox de estado (UF) a um ComboBox de cidade e um gerenciador de ComboBoxes.

    Args:
        combo_uf (QComboBox): ComboBox de estado (UF).
        combo_cidade (QComboBox): ComboBox de cidade.
        combo_manager: Gerenciador de ComboBoxes que contém o método atualizar_cidade.
    """
    # Conecta o sinal currentIndexChanged do combo_uf ao slot atualizar_cidade do combo_manager
    combo_uf.currentIndexChanged.connect(lambda: combo_manager.atualizar_cidade(combo_uf, combo_cidade))

def conectar_cliente_solicitante(combo_cliente: QComboBox, combo_solicitante: QComboBox, combo_manager):
    
    combo_cliente.currentIndexChanged.connect(lambda: combo_manager.atualizar_solicitante(combo_cliente, combo_solicitante))


def pesquisar_tabela(tabela, barra_pesquisa):
    """
    Realiza uma pesquisa na tabela ocultando linhas que não correspondem ao critério de pesquisa.

    Args:
        tabela: Tabela a ser pesquisada (deve ter rowCount() e columnCount()).
        barra_pesquisa (str): Termo de pesquisa.

    Observação:
        A pesquisa é case insensitive, ou seja, não faz distinção entre maiúsculas e minúsculas.
    """
    # Transforma o texto da barra de pesquisa em letras minúsculas
    barra_pesquisa = barra_pesquisa.lower()

    # Loop sobre as linhas da tabela
    for row in range(tabela.rowCount()):
        row_hidden = True
        # Loop sobre as colunas da tabela
        for col in range(tabela.columnCount()):
            item = tabela.item(row, col)
            # Verifica se o item não é nulo e se o texto do item contém a barra de pesquisa em letras minúsculas
            if item and barra_pesquisa in item.text().lower():
                row_hidden = False
                break

        # Esconde ou mostra a linha da tabela com base na pesquisa
        if row_hidden:
            tabela.hideRow(row)
        else:
            tabela.showRow(row)
