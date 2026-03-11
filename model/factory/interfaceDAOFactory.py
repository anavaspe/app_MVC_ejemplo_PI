from abc import abstractmethod, ABC


class InterfaceDAOFactory(ABC):
    
    @abstractmethod
    def getPedidosDAO(self):
        pass

    @abstractmethod
    def getUsuarioDAO(self, uid):
        pass