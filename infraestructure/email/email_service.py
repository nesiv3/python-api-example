import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Cargar variables de entorno (si existen)
load_dotenv()

class EmailService:
    """
    Servicio para enviar correos electrónicos con archivos adjuntos
    """
    
    def __init__(self, email_user=None, email_password=None, smtp_server="smtp.gmail.com", smtp_port=587):
        """
        Inicializa el servicio de correo electrónico.
        
        Args:
            email_user (str, optional): Dirección de correo. Por defecto usa GMAIL_USER de variables de entorno o valor predefinido.
            email_password (str, optional): Contraseña de correo. Por defecto usa GMAIL_PASSWORD de variables de entorno o valor predefinido.
            smtp_server (str, optional): Servidor SMTP. Por defecto "smtp.gmail.com".
            smtp_port (int, optional): Puerto SMTP. Por defecto 587.
        """
        # Prioridad: parámetro > variable de entorno > valor por defecto
        self.email_user = email_user or os.getenv("GMAIL_USER", "nesiv3@gmail.com")
        self.email_password = email_password or os.getenv("GMAIL_PASSWORD", "bnxk dyrr risw qcrm")
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        
        logger.info(f"Servicio de correo inicializado con usuario: {self.email_user}")
    
    def enviar_correo(self, destinatario, asunto, cuerpo, archivo_adjunto=None, nombre_archivo=None):
        """
        Envía un correo electrónico con un archivo adjunto opcional.
        
        Args:
            destinatario (str): Dirección de correo del destinatario.
            asunto (str): Asunto del correo.
            cuerpo (str): Cuerpo del correo.
            archivo_adjunto (bytes, optional): Contenido del archivo a adjuntar.
            nombre_archivo (str, optional): Nombre del archivo adjunto.
            
        Returns:
            bool: True si el envío fue exitoso, False en caso contrario.
        """
        try:
            # Configurar el servidor SMTP
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            
            # Iniciar sesión
            server.login(self.email_user, self.email_password)
            
            # Crear el mensaje
            msg = MIMEMultipart()
            msg["From"] = self.email_user
            msg["To"] = destinatario
            msg["Subject"] = asunto
            
            # Cuerpo del correo
            msg.attach(MIMEText(cuerpo, "plain"))
            
            # Adjuntar archivo si se proporciona
            if archivo_adjunto and nombre_archivo:
                part = MIMEBase("application", "octet-stream")
                part.set_payload(archivo_adjunto)
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename={nombre_archivo}")
                msg.attach(part)
            
            # Enviar el correo
            server.sendmail(self.email_user, destinatario, msg.as_string())
            
            # Cerrar la conexión
            server.quit()
            
            logger.info(f"Correo enviado con éxito a {destinatario}")
            return True
            
        except Exception as e:
            logger.error(f"Error al enviar correo: {str(e)}")
            return False
    
    def enviar_correo_cotizacion(self, destinatario, archivo_pdf, datos_cliente=None):
        """
        Envía un correo con una cotización en PDF.
        Método de conveniencia que encapsula la funcionalidad del anterior método.
        
        Args:
            destinatario (str): Dirección de correo del destinatario.
            archivo_pdf (bytes): Contenido del PDF de cotización.
            datos_cliente (dict, optional): Datos del cliente para personalizar el mensaje.
            
        Returns:
            bool: True si el envío fue exitoso, False en caso contrario.
        """
        # Personalizar el asunto y cuerpo según los datos del cliente
        nombre_cliente = datos_cliente.get("nombre", "Cliente") if datos_cliente else "Cliente"
        
        asunto = f"Tu Cotización - {nombre_cliente}"
        cuerpo = f"""Hola {nombre_cliente},

Adjunto encontrarás la cotización que solicitaste en formato PDF.

Gracias por tu interés en nuestros servicios.

Saludos cordiales,
El equipo de ventas
"""
        
        return self.enviar_correo(
            destinatario=destinatario,
            asunto=asunto,
            cuerpo=cuerpo,
            archivo_adjunto=archivo_pdf,
            nombre_archivo="cotizacion.pdf"
        )


# Ejemplo de uso directo (para pruebas)
if __name__ == "__main__":
    # Crear una instancia del servicio
    servicio_email = EmailService()
    
    # Enviar un correo de prueba
    from pathlib import Path
    
    # Para probar con un archivo real
    pdf_path = Path("ejemplo.pdf")
    if pdf_path.exists():
        with open(pdf_path, "rb") as f:
            pdf_bytes = f.read()
        
        result = servicio_email.enviar_correo_cotizacion(
            destinatario="destinatario@example.com",  # Cambiar por un correo real para pruebas
            archivo_pdf=pdf_bytes,
            datos_cliente={"nombre": "Cliente de Prueba"}
        )
        
        print(f"Resultado del envío: {'Exitoso' if result else 'Fallido'}")
    else:
        print(f"Archivo de prueba no encontrado: {pdf_path}")