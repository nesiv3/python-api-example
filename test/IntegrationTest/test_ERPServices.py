import unittest
from unittest.mock import patch, MagicMock

from infraestructure.api.ERPServices import ERPServices


class TestERPServices(unittest.TestCase):
    @patch('infraestructure.api.ERPServices.requests.get')
    def test_obtain_products_success(self, mock_get):
        # Mock the response object with a successful status code and JSON data
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [{"id": 1, "name": "Product A"}, {"id": 2, "name": "Product B"}]
        mock_get.return_value = mock_response

        # Instantiate the service and call the method
        service = ERPServices()
        result = service.obtain_products()

        # Assert the result matches the mocked data
        self.assertEqual(result, [{"id": 1, "name": "Product A"}, {"id": 2, "name": "Product B"}])
        mock_get.assert_called_once_with("https://crmniv.azurewebsites.net/api/Products", timeout=400)

    @patch('infraestructure.api.ERPServices.requests.get')
    def test_obtain_products_failure(self, mock_get):
        # Mock the response object with a failure status code
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        # Instantiate the service and call the method
        service = ERPServices()
        result = service.obtain_products()

        # Assert the result is an empty list
        self.assertEqual(result, [])
        mock_get.assert_called_once_with("https://crmniv.azurewebsites.net/api/Products", timeout=400)

if __name__ == '__main__':
    unittest.main()