from ....dao.interfacePedidosDAO import InterfacePedidoDAO
from ....dto.pedidosDTO import pedidoDTO, PedidosDTO


class FirebasePedidosDAO(InterfacePedidoDAO):

    def __init__(self, collection):
        self.collection = collection
    
    def get_Pedidos(self):
        pedidos = PedidosDTO()
        try:
            query = self.collection.stream()
            for doc in query:
                pedido_data = doc.to_dict()  # Convierte el documento a un diccionario
                
                # Crear un objeto pedidoDTO
                pedido_dto = pedidoDTO()
                pedido_dto.id = doc.id  # ID del documento en Firestore
                pedido_dto.cliente = pedido_data.get("cliente", "")
                pedido_dto.evento = pedido_data.get("evento", "")
                pedido_dto.numEntradas = pedido_data.get("numEntradas", "")
                pedido_dto.total = pedido_data.get("total", "")
                pedido_dto.estado = pedido_data.get("estado", 0)
                pedido_dto.fecha = pedido_data.get("fecha", 0.0)
                # Transformar a JSON previo a append
                pedidos.insertPedido(pedido_dto.pedidodto_to_dict())  # Agregar el pedido a la lista
        except Exception as e:
            print(e)

        return pedidos.pedidolist_to_json()