from services.pedido_service import PedidoService
from repositories.pedido_repository import PedidoRepository  # Import do repositório
from database.connection import DatabaseConnection
from models.desconto import DescontoNormal, DescontoVIP, DescontoPremium
from models.pedido import Pedido

if __name__ == "__main__":
    # 1. Instancia o repositório
    repository = PedidoRepository(DatabaseConnection())
    
    # 2. Injeta o repositório no serviço
    service = PedidoService(repository)

    # 3. Criando pedidos
    pedido1 = Pedido("Cliente A", DescontoNormal())
    pedido1.valor_original = 100.0

    pedido2 = Pedido("Cliente B", DescontoVIP())
    pedido2.valor_original = 200.0

    pedido3 = Pedido("Cliente C", DescontoPremium())
    pedido3.valor_original = 300.0

    # 4. Adicionando e processando
    service.adicionar_pedido(pedido1)
    service.adicionar_pedido(pedido2)
    service.adicionar_pedido(pedido3)

    service.processar_pedidos()