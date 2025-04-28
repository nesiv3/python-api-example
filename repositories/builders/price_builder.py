class PriceBuilder:
    """
    Builder para construir la estructura de una cotización.
    """

    def __init__(self):
        self.quote = {}

    def add_client(self, client):
        """
        Añade la información del cliente a la cotización.

        Args:
            client (dict): Información del cliente.

        Returns:
            QuoteBuilder: Retorna la instancia del builder para encadenar métodos.
        """
        self.quote["cliente"] = client
        return self

    def add_products(self, products):
        """
        Añade la lista de productos a la cotización.

        Args:
            products (list): Lista de productos.

        Returns:
            QuoteBuilder: Retorna la instancia del builder para encadenar métodos.
        """
        self.quote["productos"] = products
        return self

    def add_totals(self, total):
        """
        Añade el total de la cotización.

        Args:
            total (float): Total de la cotización.

        Returns:
            QuoteBuilder: Retorna la instancia del builder para encadenar métodos.
        """
        self.quote["total_orden"] = total
        return self

    def build(self):
        """
        Construye y retorna la cotización completa.

        Returns:
            dict: Cotización completa.
        """
        return {"orden": self.quote}