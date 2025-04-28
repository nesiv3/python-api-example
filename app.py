from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger
from repositories.price_repository import PriceRepository
import json

from services.price import PriceServices  # Si usas JSON
from services.products import ProductsServices
from infraestructure.email.email_service import EmailService
from utils.factory import ServiceFactory

# Crear instancias de servicios
products_service = ProductsServices()
email_service = EmailService()
crm_service = ServiceFactory.get_service("CRM")

# Inyectar dependencias al repositorio
price_repository = PriceRepository(products_service, email_service, crm_service)
price_service = PriceServices(price_repository)

app = Flask(__name__)
api = Api(app)


# Cargar el template desde un archivo JSON
with open('./config/swagger_template.json', 'r') as f:
    template = json.load(f)

# Configurar Swagger con el template cargado
swagger = Swagger(app, template=template)

class CreatePrice(Resource):
    def post(self):
        """
        Este método responde a una solicitud POST para procesar un arreglo de objetos tipo Product.
        ---
        tags:
        - Products
        parameters:
          - in: body
            name: body
            required: true
            schema:
              type: array
              items:
                $ref: '#/definitions/OrderRequest'  # Cambia de "#/components/schemas/Product" a "#/definitions/Product"
        responses:
            200:
                description: Solicitud POST exitosa
                schema:
                    type: object
                    properties:
                        message:
                            type: string
                            description: Mensaje de éxito
        """
     

    
        return price_service.create_price(request.json)



api.add_resource(CreatePrice, "/price")

if __name__ == "__main__":
    app.run(debug=True)
