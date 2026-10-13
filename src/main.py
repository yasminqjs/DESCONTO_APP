from app.frameworks.database.memory_database import MemoryDatabase
from app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from app.use_cases.criar_pedido import CriarPedido
from app.adapters.controllers.pedido_controller import PedidoController

def main() -> None:
    # Inicializar o banco de dados em memória
    database = MemoryDatabase()

    # Inicializar o repositório de pedidos
    pedido_gateway = MemoryPedidoRepository(database)

    # Inicializar o caso de uso CriarPedido
    criar_pedido_use_case = CriarPedido(pedido_gateway)

    # Inicializar o controlador de pedidos
    controller = PedidoController(criar_pedido_use_case)

    # Exemplo de criação de pedidos
    pedido1 = controller.criar_pedido("Cliente A", 100.0, "normal")
    pedido2 = controller.criar_pedido("Cliente B", 200.0, "vip")
    pedido3 = controller.criar_pedido("Cliente C", 300.0, "premium")

    print("Pedidos criados:")
    print(pedido1.cliente, pedido1.valor_original, pedido1.valor_final())
    print(pedido2.cliente, pedido2.valor_original, pedido2.valor_final())
    print(pedido3.cliente, pedido3.valor_original, pedido3.valor_final())

if __name__ == "__main__":
    main()