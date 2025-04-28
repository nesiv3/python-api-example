import requests

from utils.factory import ServiceFactory

erp_service = ServiceFactory.get_service("ERP")


class ProductsServices:
    def __init__(self):
        """
        Constructor de la clase ProductsServices.
        Esta clase se encarga de interactuar con la API de productos.
        """
        pass

    def obtain_Products_Price_By_Ids(self, product_ids):
        """
        This function obtains products by their IDs from the API.

        Args:
            product_ids (list): A list of product IDs to retrieve

        Returns:
            list: A list of products that match the provided IDs
        """
        if not product_ids or not isinstance(product_ids, list):
            return {"error": "Invalid input: product_ids must be a non-empty list"}

        # Get all products first
        all_products = erp_service.obtain_products()
        print(all_products)
        # If the API call failed, return empty list
        if not all_products:
            return []
        print(product_ids)
        product_id_list = [product["id"] for product in product_ids]
        # Filter products by the IDs in the input list
        filtered_products = [
            product for product in all_products if product.get('id') in product_id_list]

        return {
            "products": filtered_products,
            "count": len(filtered_products),
            "peticion": self.format_products(filtered_products, product_ids),
            "requested_ids": product_ids
        }

    def format_products(self, filtered_products, product_ids):
        """
        Transforma los datos de respuesta para obtener un diccionario 
        con nombres de productos y sus cantidades.

        Args:
            response_data (dict): Datos de respuesta original

        Returns:
            dict: Diccionario con nombres de productos y cantidades
        """
        result = []  # Elimina el espacio extra al inicio de esta línea

        # Crear un mapa de id -> cantidad desde requested_ids
        quantities_map = {item["id"]: item["cantidad"] for item in product_ids}

        # Crear el diccionario resultado con nombre -> cantidad
        for product in filtered_products:
            product_id = product.get("id")
            product_name = product.get("name", "Producto sin nombre")
            price = product.get("price", 0)
            quantity = quantities_map.get(product_id, 0)

             # Calcular el total para este producto
            item_total = price * quantity
          
            
            # Almacenar toda la información relevante para este producto
            result.append({
                "nombre": product_name,
                "cantidad": quantity,
                "precio": price,                
                "total": item_total
            })

        return result
