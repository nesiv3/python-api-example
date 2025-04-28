from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from strategies.pdf_strategy import PDFStrategy


# Tasa Representativa del Mercado (TRM) para convertir COP a USD
TRM = 4338.36  # Este TRM puede traerse desde fuera si deseas parametrizarlo

class StandardPDFStrategy(PDFStrategy):
    """
    Estrategia para generar un PDF estándar.
    """

    def generate(self, data: dict) -> bytes:
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        # Encabezado
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, height - 50, "COTIZACIÓN DE FLORES – FLORES ELEGANCIA NATURAL (EST)")
        p.setFont("Helvetica", 10)
        p.drawString(50, height - 70, f"Cliente: {data['orden']['cliente']['nombre_completo']}")
        p.drawString(50, height - 85, f"Email: {data['orden']['cliente']['email']}")
        p.drawString(50, height - 100, f"Total: ${data['orden']['total_orden']} COP")

        # Detalle de productos
        y = height - 130
    
        # Guardar el PDF
        p.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        return pdf_data
