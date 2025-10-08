from restaurant.models import MenuItem
from django.test import TestCase


class MenuViewTests(TestCase):
    def setUp(self):
        self.menu_item1 = MenuItem.objects.create(id = 1, title="Pizza", price=150, inventory=50)
        self.menu_item2 = MenuItem.objects.create(id = 2, title="Pasta", price=120, inventory=30)

    def test_get_menu_items(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], "Pizza")
        self.assertEqual(response.data[1]['title'], "Pasta")

    def test_get_single_menu_item(self):
        response = self.client.get(f'/menu/{self.menu_item1.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], "Pizza")
        self.assertEqual(response.data['price'], '150.00')
