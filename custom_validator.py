from PySide6.QtGui import QValidator

class CustomValidator(QValidator):
    def __init__(self, parent=None):
        super().__init__(parent)

    def validate(self, input_text, pos):
        # Remover qualquer caractere de formatação do texto de entrada
        cleaned_text = ''.join(filter(str.isdigit, input_text))

        # Aplicar a máscara (00) 0 0000-0000
        if len(cleaned_text) == 0:
            return QValidator.Intermediate  # Campo vazio, ainda não é válido nem inválido
        elif len(cleaned_text) <= 2:
            formatted_text = "(" + cleaned_text
        elif len(cleaned_text) <= 3:
            formatted_text = "(" + cleaned_text[:2] + ") " + cleaned_text[2]
        elif len(cleaned_text) <= 7:
            formatted_text = "(" + cleaned_text[:2] + ") " + cleaned_text[2] + " " + cleaned_text[3:]
        else:
            formatted_text = "(" + cleaned_text[:2] + ") " + cleaned_text[2] + " " + cleaned_text[3:7] + "-" + cleaned_text[7:]
        
        # Atualizar o texto do QLineEdit com a máscara aplicada
        self.parent().setText(formatted_text)

        # Verificar se o texto de entrada corresponde ao texto formatado
        if formatted_text == input_text:
            return QValidator.Acceptable  # Texto válido
        else:
            return QValidator.Intermediate  # Texto inválido, mas ainda pode ser modificado
