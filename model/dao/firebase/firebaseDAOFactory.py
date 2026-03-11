from ...factory.interfaceDAOFactory import InterfaceDAOFactory
from .collection.firebasePedidosDAO import FirebasePedidosDAO
from .collection.firebaseUsuarioDAO import FirebaseUsuarioDAO
from .firebaseConnector import FirebaseConnector

class FirebaseDAOFactory (InterfaceDAOFactory):
    def __init__(self):
        self.connector = FirebaseConnector()
    
    def getPedidosDAO(self):
        return FirebasePedidosDAO(self.connector.get_pedidos_collection())
    
    def getUsuarioDAO(self, uid):
        return FirebaseUsuarioDAO(self.connector.get_usuario_by_uid(uid))