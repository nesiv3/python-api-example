from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from datetime import datetime

TRM = 4338.36  # Este TRM puede traerse desde fuera si deseas parametrizarlo

def generar_pdf_cotizacion(orden: dict) -> bytes:
    cliente = orden["orden"]["cliente"]
    productos = orden["orden"]["productos"]
    total_cop = orden["orden"]["total_orden"]
    total_usd = round(total_cop / TRM, 2)

    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

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

    y -= 30
    p.setFont("Helvetica-Bold", 11)
    p.drawString(50, y, "Detalle de productos")
    y -= 20

    p.setFont("Helvetica", 10)
    for pdt in productos:
        precio_usd = round(pdt["precio"] / TRM, 2)
        total_usd_item = round(pdt["total"] / TRM, 2)
        p.drawString(50, y, f"- {pdt['nombre']} x {pdt['cantidad']} @ ${pdt['precio']} COP "
                             f"(~${precio_usd} USD): ${pdt['total']} COP / ~${total_usd_item} USD")
        y -= 15

    y -= 10
    p.setFont("Helvetica-Bold", 10)
    p.drawString(50, y, f"Total en COP: ${total_cop:,}")
    y -= 15
    p.drawString(50, y, f"Total en USD: ~${total_usd}")
    y -= 15
    p.setFont("Helvetica", 9)
    p.drawString(50, y, f"* TRM usada: $ {TRM} COP/USD")

    y -= 30
    p.setFont("Helvetica", 9)
    p.drawString(50, y, "Condiciones:")
    y -= 15
    p.drawString(60, y, "- Cotización válida por 7 días hábiles.")
    y -= 15
    p.drawString(60, y, "- Para confirmar el pedido, responda al correo del asesor.")

    p.save()
    pdf_data = buffer.getvalue()
    buffer.close()
    return pdf_data
