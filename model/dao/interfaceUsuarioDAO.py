from abc import ABC, abstractmethod

class InterfaceUsuarioDAO(ABC):

    @abstractmethod
    def get_usuario(self, uid):
        pass