class Protocolo:
    def __init__(self, id, data, cliente, solicitante, consultor, tipo_atendimento,
                 relatorio, hora_inicio, hora_termino, cancelado):
        """
        Inicializa os atributos do objeto Protocolo com os valores fornecidos.

        Parâmetros:
        - id: Identificador único do protocolo.
        - data: Data do protocolo.
        - cliente: Cliente associado ao protocolo.
        - solicitante: Solicitante do protocolo.
        - consultor: Consultor responsável pelo protocolo.
        - tipo_atendimento: Tipo de atendimento do protocolo.
        - relatorio: Relatório do protocolo.
        - hora_inicio: Hora de início do protocolo.
        - hora_termino: Hora de término do protocolo.
        - cancelado: Indica se o protocolo foi cancelado ou não.
        """
        self.id = id
        self.data = data
        self.cliente = cliente
        self.solicitante = solicitante
        self.consultor = consultor
        self.tipo_atendimento = tipo_atendimento
        self.relatorio = relatorio
        self.hora_inicio = hora_inicio
        self.hora_termino = hora_termino
        self.cancelado = cancelado

    def __str__(self):
        """
        Retorna uma representação em string do objeto Protocolo.
        """
        return f"Protocolo: ({self.id}) {self.data}"
