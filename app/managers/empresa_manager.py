import base64
from PySide6.QtGui import QPixmap
from app.managers.data_manager import DataManager

class EmpresaManager:
    def __init__(self, ui):
        self.ui = ui
        self.data = DataManager()  # Instancia o DataManager para acessar os dados das empresas

    def carregar_empresa(self):
        
        empresas = self.data.buscar_empresa()  # Obtenha as empresas do banco de dados

        # Verifique se há empresas no banco
        if empresas:
            # Se houver empresas, pegue a primeira empresa da lista
            empresa = empresas[0]
            
            # Preencha os line edits da interface com os dados da empresa
            self.ui.ed_empresaId.setText(str(empresa.id))
            self.ui.ed_empresaRazaoSocial.setText(empresa.razao_social)
            self.ui.ed_empresaCpfCnpj.setText(str(empresa.cpf_cnpj))
            self.ui.ed_empresaContato.setText(empresa.contato)
            self.ui.ed_empresaEmail.setText(empresa.email)
            self.ui.ed_empresaCep.setText(empresa.endereco_cep)
            self.ui.ed_empresaLogradouro.setText(empresa.endereco_logradouro)
            self.ui.ed_empresaNumero.setText(str(empresa.endereco_numero))
            self.ui.ed_empresaBairro.setText(empresa.endereco_bairro)
            self.ui.ed_empresaReferencia.setText(empresa.endereco_referencia)
            self.ui.cb_empresaUf.setCurrentText(empresa.uf)
            self.ui.cb_empresaCidade.setCurrentText(empresa.cidade)

            # Carrega e exibe a imagem da empresa
            if empresa.logo:
                # Decodifica a string base64 de volta para bytes
                imagem_bytes = base64.b64decode(empresa.logo)
                pixmap = QPixmap()
                pixmap.loadFromData(imagem_bytes)
                self.ui.logoEmpresa.setPixmap(pixmap)
                self.ui.logoEmpresa.setScaledContents(True)  # Redimensiona a imagem para caber na label
            else:
                # Caso a empresa não tenha logo, faz alguma ação específica
                print("Aviso: A empresa não possui uma logo.")
                default_image_path = 'assets/icons/logo_p_dark_200px.png'
                pixmap = QPixmap(default_image_path)
                self.ui.logoEmpresa.setPixmap(pixmap)
                self.ui.logoEmpresa.setScaledContents(True)  # Redimensiona a imagem para caber na label

            # Marca o RadioButton Jurídica se a natureza for jurídica
            if empresa.natureza_social == "Jurídica":
                self.ui.radioButton_empresaJuridica.setChecked(True)
            else:
                self.ui.radioButton_empresaFisica.setChecked(True)
            
            # Bloquear a edição dos campos de texto
            self.ui.ed_empresaId.setReadOnly(True)
            self.ui.ed_empresaRazaoSocial.setReadOnly(True)
            self.ui.ed_empresaCpfCnpj.setReadOnly(True)
            self.ui.ed_empresaContato.setReadOnly(True)
            self.ui.ed_empresaEmail.setReadOnly(True)
            self.ui.ed_empresaCep.setReadOnly(True)
            self.ui.ed_empresaLogradouro.setReadOnly(True)
            self.ui.ed_empresaNumero.setReadOnly(True)
            self.ui.ed_empresaBairro.setReadOnly(True)
            self.ui.ed_empresaReferencia.setReadOnly(True)

            # Bloquear a seleção dos combo boxes
            self.ui.cb_empresaUf.setEnabled(False)
            self.ui.cb_empresaCidade.setEnabled(False)

            # Bloquear a seleção dos radio buttons
            self.ui.radioButton_empresaJuridica.setEnabled(False)
            self.ui.radioButton_empresaFisica.setEnabled(False)
        else:
            print("Nenhuma empresa encontrada no banco de dados.")
            # Você pode adicionar aqui um tratamento específico para quando nenhuma empresa for encontrada
