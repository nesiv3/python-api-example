from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from strategies.pdf_strategy import PDFStrategy


TRM = 4338.36  # Este TRM puede traerse desde fuera si deseas parametrizarlo
class DetailedPDFStrategy(PDFStrategy):
    """
    Estrategia para generar un PDF Estandar.
    """
    
    def generate(self, data: dict) -> bytes:
   
    
        """
        Genera un archivo PDF con la cotización de productos basada en los datos proporcionados.

        Pasos:
        1. Extrae la información del cliente, productos y totales desde el diccionario `orden`.
        2. Crea un archivo PDF utilizando la biblioteca ReportLab.
        3. Añade detalles como cliente, productos, totales y condiciones al PDF.
        4. Devuelve el contenido del PDF como un objeto de bytes.

        Args:
            orden (dict): Diccionario que contiene la información de la orden. Debe incluir:
                - orden["cliente"]: Información del cliente (nombre, email, dirección, tipo).
                - orden["productos"]: Lista de productos con detalles como nombre, precio, cantidad y total.
                - orden["total_orden"]: Total de la orden en COP.

        Returns:
            bytes: Contenido del archivo PDF generado.
        """
        # Extraer información del cliente y productos desde el diccionario de la orden
        cliente = data["orden"]["cliente"]
        productos = data["orden"]["productos"]
        total_cop = data["orden"]["total_orden"]
        total_usd = round(total_cop / TRM, 2)  # Convertir el total a USD usando la TRM

        # Crear un buffer en memoria para almacenar el PDF
        buffer = BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        # Configurar el encabezado del PDF
        y = height - 50
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, y, "COTIZACIÓN DE FLORES – FLORES ELEGANCIA NATURAL")
        y -= 25
        p.setFont("Helvetica", 10)
        p.drawString(50, y, f"Fecha: {datetime.utcnow().strftime('%Y-%m-%d')}")
        y -= 20
        p.drawString(50, y, f"Cliente: {cliente['nombre_completo']} ({cliente['tipo']})")
        y -= 15
        p.drawString(50, y, f"Email: {cliente['email']}")
        y -= 15
        p.drawString(50, y, f"Dirección: {cliente['direccion']}")

        # Añadir el detalle de los productos
        y -= 30
        p.setFont("Helvetica-Bold", 11)
        p.drawString(50, y, "Detalle de productos")
        y -= 20

        p.setFont("Helvetica", 10)
        for pdt in productos:
            # Calcular precios en USD para cada producto
            precio_usd = round(pdt["precio"] / TRM, 2)
            total_usd_item = round(pdt["total"] / TRM, 2)
            p.drawString(50, y, f"- {pdt['nombre']} x {pdt['cantidad']} @ ${pdt['precio']} COP "
                                f"(~${precio_usd} USD): ${pdt['total']} COP / ~${total_usd_item} USD")
            y -= 15

        # Añadir los totales en COP y USD
        y -= 10
        p.setFont("Helvetica-Bold", 10)
        p.drawString(50, y, f"Total en COP: ${total_cop:,}")
        y -= 15
        p.drawString(50, y, f"Total en USD: ~${total_usd}")
        y -= 15
        p.setFont("Helvetica", 9)
        p.drawString(50, y, f"* TRM usada: $ {TRM} COP/USD")

        # Añadir las condiciones de la cotización
        y -= 30
        p.setFont("Helvetica", 9)
        p.drawString(50, y, "Condiciones:")
        y -= 15
        p.drawString(60, y, "- Cotización válida por 7 días hábiles.")
        y -= 15
        p.drawString(60, y, "- Para confirmar el pedido, responda al correo del asesor.")

        # Guardar el PDF y devolverlo como bytes
        p.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        return pdf_data
