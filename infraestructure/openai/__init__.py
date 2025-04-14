import azure.functions as func
from infraestructure.openai.pdf_generator import generar_pdf_cotizacion
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        orden = req.get_json()
        pdf_bytes = generar_pdf_cotizacion(orden)

        return func.HttpResponse(
            pdf_bytes,
            mimetype="application/pdf",
            headers={"Content-Disposition": "attachment; filename=cotizacion.pdf"}
        )

    except Exception as e:
        return func.HttpResponse(f"Error procesando la orden: {str(e)}", status_code=500)
