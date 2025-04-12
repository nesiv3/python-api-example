from infraestructure.api.CRM_Services import CRM_Services
from services.products import ProductsServices

products_service = ProductsServices()
crm_services = CRM_Services()  # Ensure CRM_Services is a class and properly imported

class PriceRepository:
    """
    Clase que maneja las operaciones de base de datos para las cotizaciones.
    """

    def __init__(self):
        """
        Inicializa el repositorio de cotizaciones.

        """

    def create_price(self, info):
        """
        Crea una nueva cotización en la base de datos.

        Args:
            cotizacion_data (dict): Datos de la cotización a crear.

        Returns:
            dict: Cotización creada, incluyendo su ID.
        """
      # Revisar los productos existentes y su valor desde el servicio
        products_all = []
        user_ids = []
        order_data = {}
        for order_request in info:
            products_all.extend(order_request.get("products", []))
            user_ids.append(order_request.get("userId"))

        existing_products = products_service.obtain_Products_Price_By_Ids(
            products_all)
        info_user = crm_services.obtain_user_by_id(user_ids[0])

        order_data =  {
            "products": existing_products,
            "user": info_user,
            "client": user_ids,         
        }
        return self.extract_order_summary(order_data)

    def extract_order_summary(self,order_data):  
        """
        Extrae la información relevante de una orden y la consolida en un único objeto.
        
        Args:
            order_data (dict): Datos completos de la orden
            
        Returns:
            dict: Objeto simplificado con información del usuario y los productos
        """
        # Extraer información del usuario
        user_info = order_data.get("user", {})
        
        # Extraer productos de la petición
        products_info = order_data.get("products", {}).get("peticion", [])
        
        # Calcular el total general
        total_order = sum(item.get("total", 0) for item in products_info)
        
        # Construir el objeto consolidado
        summary = {
            "orden": {
                "cliente": {
                    "nombre_completo": f"{user_info.get('nombre', '')} {user_info.get('apellido', '')}",
                    "email": user_info.get("email", ""),
                    "direccion": user_info.get("direccion", ""),
                    "tipo": user_info.get("tipo_usuario", "")
                },
                "productos": products_info,
                "total_orden": total_order,
               
            }
        }
        
        return summary
