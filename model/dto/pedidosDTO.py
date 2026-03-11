import json

class PedidosDTO():
    def __init__(self):
        self.pedidolist = []

    def insertPedido(self, elem):
        self.pedidolist.append(elem)

    def pedidolist_to_json(self):
        return json.dumps(self.pedidolist)

class pedidoDTO():
    def __init__(self):
        self.id = None
        self.cliente = None
        self.evento = None
        self.numEntradas = None
        self.total = None
        self.estado = None
        self.fecha = None

    def is_Empty(self):
        return (self.id is None and self.cliente is None and self.id is None and
                self.evento is None and self.numEntradas is None and self.total is None
                and self.estado is None and self.fecha is None)

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_cliente(self):
        return self.cliente

    def set_cliente(self, cliente):
        self.cliente = cliente

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_evento(self):
        return self.evento

    def set_evento(self, evento):
        self.evento = evento

    def get_numEntradas(self):
        return self.numEntradas

    def set_numEntradas(self, numEntradas):
        self.numEntradas = numEntradas

    def get_total(self):
        return self.total

    def set_total(self, total):
        self.total = total

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    def pedidodto_to_dict(self):
        return {
            "id": self.id,
            "cliente": self.cliente,
            "id": self.id,
            "evento": self.evento,
            "numEntradas": self.numEntradas,
            "total": self.total,
            "estado": str(self.estado),
            "fecha": self.fecha
        }