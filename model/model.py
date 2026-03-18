from .factory import interfaceDAOFactory

class Model ():
    # Tiene que crear el factory de firebase
    # Tiene que obtener lo DAO
    def __init__(self, factory: interfaceDAOFactory):
        self.factory = factory
        self.usuarioDAO = None
        try:
            self.pedidoDAO = self.factory.getPedidosDAO()
        except Exception as e:
            print(f"Error initializing DAOs: {e}")
            raise
    
    def get_pedidos(self):
        return self.pedidoDAO.get_Pedidos()
    
    def get_usuario(self, uid):
        usuarioDAO = self.factory.getUsuarioDAO(uid)
        return usuarioDAO.get_usuario(uid)
    
#Cuando se instancie el modelo, se le pasará la factory de firebase, y el modelo se encargará de obtener los DAO necesarios para su funcionamiento.