class ServiceFactory:
    """
    Clase Factory para crear instancias de servicios.
    Centraliza la lógica de creación de servicios como ERPServices y CrmServices.
    """

    @staticmethod
    def get_service(service_name):
        """
        Devuelve una instancia del servicio solicitado.

        Args:
            service_name (str): Nombre del servicio a instanciar (por ejemplo, "ERP" o "CRM").

        Returns:
            object: Instancia del servicio solicitado.

        Raises:
            ValueError: Si el nombre del servicio no es válido.
        """
        if service_name == "ERP":
            from infraestructure.api.ERPServices import ERPServices
            return ERPServices()
        elif service_name == "CRM":
            from infraestructure.api.CRMServices import CrmServices
            return CrmServices()
        else:
            raise ValueError(f"Servicio desconocido: {service_name}")