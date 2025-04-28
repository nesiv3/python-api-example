from strategies.pdf_strategy import PDFStrategy

class PDFContext:
    """
    Contexto para manejar estrategias de generación de PDFs.
    """

    def __init__(self, strategy: PDFStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: PDFStrategy):
        """
        Cambia la estrategia actual.

        Args:
            strategy (PDFStrategy): Nueva estrategia a usar.
        """
        self.strategy = strategy

    def generate_pdf(self, data: dict) -> bytes:
        """
        Genera un PDF usando la estrategia actual.

        Args:
            data (dict): Datos necesarios para generar el PDF.

        Returns:
            bytes: Contenido del archivo PDF generado.
        """
        return self.strategy.generate(data)