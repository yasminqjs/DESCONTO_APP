class CriarPedidoOutputDTO:
    def __init__(self, cliente: str, valor_original: float,valor_desconto: float, tipo_desconto: str, valor_final: float):
        self.cliente = cliente
        self.valor_original = valor_original
        self.valor_desconto = valor_desconto
        self.tipo_desconto = tipo_desconto
        self.valor_final = valor_final