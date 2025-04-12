class PriceServices:
    def __init__(self, price_repository):
        self.price_repository = price_repository

    def create_price(self, info):
        """
        Crea una nueva cotización en la base de datos.

        Args:
            cotizacion_data (dict): Datos de la cotización a crear.

        Returns:
            dict: Respuesta de la creación de la cotización.
        """
        return self.price_repository.create_price(info)