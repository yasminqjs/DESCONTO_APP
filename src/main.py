from app.frameworks.database.memory_database import MemoryDatabase
from app.adapters.repositories.memory_pedido_repository import MemoryPedidoRepository
from app.use_cases.criar_pedido import CriarPedido
from app.adapters.controllers.pedido_controller import PedidoController
from app.presenters.pedido_presenter import PedidoPresenter

def main() -> None:
    # Inicializar o banco de dados em memória
    database = MemoryDatabase()

    # Inicializar o repositório de pedidos
    pedido_gateway = MemoryPedidoRepository(database)

    # Inicializar o caso de uso CriarPedido
    criar_pedido_use_case = CriarPedido(pedido_gateway)

    # Inicializar o controlador de pedidos
    presenter = PedidoPresenter()
    controller = PedidoController(criar_pedido_use_case, presenter)

    # Exemplo de criação de pedidos
    pedido1 = controller.criar_pedido("Cliente A", 100.0, "normal")
    pedido2 = controller.criar_pedido("Cliente B", 200.0, "vip")
    pedido3 = controller.criar_pedido("Cliente C", 300.0, "premium")

    print("Pedidos criados:")
    for pedido in (pedido1, pedido2, pedido3):
        print(pedido)

    print("\nTodos os pedidos:")
    for pedido in controller.listar_pedidos():
        print(pedido)

if __name__ == "__main__":
    main()