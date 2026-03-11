from abc import ABC, abstractmethod
from typing import List, Optional

class InterfacePedidoDAO(ABC):

    @abstractmethod
    def get_Pedidos(self):
        pass