from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import Product

# Create your tests here.
class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            description="Gaming laptop",
            price=75000.00,
            stock_quantity=10,
            category="Electronics"
        )
        self.list_url = reverse('product-list')

    def test_create_product(self):
        data = {
            "name": "Mouse",
            "description": "Wireless mouse",
            "price": 1200.50,
            "stock_quantity": 50,
            "category": "Accessories"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
        self.assertEqual(Product.objects.get(name="Mouse").price, 1200.50)

    def test_get_product_list(self):
        response = self.client.get(self.list_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_get_product_detail(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Laptop')

    def test_update_product(self):
        url = reverse('product-detail', args=[self.product.id])
        updated_data = {
            "name": "Laptop Pro",
            "description": "High-end gaming laptop",
            "price": 85000.00,
            "stock_quantity": 5,
            "category": "Electronics"
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.price, 85000.00)

    def test_delete_product(self):
        url = reverse('product-detail', args=[self.product.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_invalid_price(self):
        data = {
            "name": "Keyboard",
            "description": "Mechanical keyboard",
            "price": -500.00,
            "stock_quantity": 20,
            "category": "Accessories"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("Price must be greater than zero.", str(response.data))