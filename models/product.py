class Product:
    def __init__(self, id, cantidad):
        self.id = id
        self.cantidad = cantidad

    def to_dict(self):
        return {"id": self.id, "cantidad": self.cantidad}