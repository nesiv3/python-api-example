from services.context.pdf_context import PDFContext
from strategies.standard_pdf_strategy import StandardPDFStrategy
from strategies.detailed_pdf_strategy import DetailedPDFStrategy
# Tasa Representativa del Mercado (TRM) para convertir COP a USD
TRM = 4338.36  # Este TRM puede traerse desde fuera si deseas parametrizarlo

def generar_pdf_cotizacion(orden: dict,tipo: str="detallado") -> bytes:
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
    if tipo == "detallado":
        strategy = DetailedPDFStrategy()
    else:
        strategy = StandardPDFStrategy()

    context = PDFContext(strategy)
    return context.generate_pdf(orden)
