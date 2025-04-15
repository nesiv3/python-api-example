import unittest
from unittest.mock import patch, MagicMock
from app import app

class TestCreatePrice(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    @patch('app.price_service.create_price')
    def test_post_success(self, mock_create_price):
        # Mock the service response
        mock_create_price.return_value = {"message": "Precio creado exitosamente"}

        # Define the payload
        payload = [
            {"product_id": 1, "price": 100},
            {"product_id": 2, "price": 200}
        ]

        # Make the POST request
        response = self.app.post('/price', json=payload)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Precio creado exitosamente"})
        mock_create_price.assert_called_once_with(payload)

    @patch('app.price_service.create_price')
    def test_post_invalid_payload(self, mock_create_price):
        # Mock the service response
        mock_create_price.side_effect = ValueError("Invalid payload")

        # Define an invalid payload
        payload = {"invalid": "data"}

        # Make the POST request
        response = self.app.post('/price', json=payload)

        # Assertions
        self.assertEqual(response.status_code, 500)  # Assuming the app handles this as a server error
        mock_create_price.assert_called_once_with(payload)

if __name__ == '__main__':
    unittest.main()