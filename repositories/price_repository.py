from repositories.builders.price_builder import PriceBuilder
from utils.factory import ServiceFactory
from services.pdf_generator import generar_pdf_cotizacion
from utils.decorators import log_execution

# Corrected module path and function name
from infraestructure.email.email_service import EmailService
from services.products import ProductsServices

products_service = ProductsServices()
email_service = EmailService()
crm_service = ServiceFactory.get_service("CRM")



class PriceRepository:
    """
    Clase que maneja las operaciones de base de datos para las cotizaciones.
    """

    def __init__(self, products_service, email_service, crm_service):
        """
        Inicializa el repositorio de cotizaciones con las dependencias necesarias.

        Args:
            products_service (ProductsServices): Servicio para manejar productos.
            email_service (EmailService): Servicio para enviar correos electrónicos.
            crm_service (CrmServices): Servicio para manejar datos de usuarios.
        """
        self.products_service = products_service
        self.email_service = email_service
        self.crm_service = crm_service

    @log_execution
    def create_price(self, info):
        """
        Crea una nueva cotización en la base de datos.

        Args:
            info (list): Lista de solicitudes de orden con productos y usuario.

        Returns:
            dict: Cotización creada, incluyendo su ID.
        """
        products_all = []
        user_ids = []
        order_data = {}

        for order_request in info:
            products_all.extend(order_request.get("products", []))
            user_ids.append(order_request.get("userId"))
            type_price = order_request.get("type_price")

        # Usa las dependencias inyectadas
        existing_products = self.products_service.obtain_Products_Price_By_Ids(products_all)
        info_user = self.crm_service.obtain_user_by_id(user_ids[0])

        order_data = {
            "products": existing_products,
            "user": info_user,
            "client": user_ids,
        }
        return self.extract_order_summary(order_data, type_price)

    @log_execution
    def extract_order_summary(self, order_data, type_price="detallado"):
        """
        Extrae la información relevante de una orden y la consolida en un único objeto.

        Args:
            order_data (dict): Datos completos de la orden.

        Returns:
            dict: Objeto simplificado con información del usuario y los productos.
        """
        user_info = order_data.get("user", {})
        products_info = order_data.get("products", {}).get("peticion", [])
        total_order = sum(item.get("total", 0) for item in products_info)

        # Usa el Builder para construir la cotización
        builder = PriceBuilder()
        summary = (
            builder
            .add_client({
                "nombre_completo": f"{user_info.get('nombre', '')} {user_info.get('apellido', '')}",
                "email": user_info.get("email", ""),
                "direccion": user_info.get("direccion", ""),
                "tipo": user_info.get("tipo_usuario", "")
            })
            .add_products(products_info)
            .add_totals(total_order)
            .build()
        )

        # Genera el PDF con la cotización
        pdf_bytes = generar_pdf_cotizacion(summary, type_price)

        # Usa el servicio de correo inyectado
        result = self.email_service.enviar_correo_cotizacion(
            destinatario=user_info.get("email", "nesiv3@hotmail.com"),
            archivo_pdf=pdf_bytes,
            datos_cliente={"nombre": "Cliente de Prueba"}
        )

        return result
