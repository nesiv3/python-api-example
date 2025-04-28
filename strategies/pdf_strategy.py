from abc import ABC, abstractmethod

class PDFStrategy(ABC):
    """
    Interfaz base para las estrategias de generación de PDFs.
    """

    @abstractmethod
    def generate(self, data: dict) -> bytes:
        """
        Genera un archivo PDF basado en los datos proporcionados.

        Args:
            data (dict): Datos necesarios para generar el PDF.

        Returns:
            bytes: Contenido del archivo PDF generado.
        """
        pass