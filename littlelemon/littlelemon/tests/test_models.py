from django.test import TestCase
from restaurant.models import Menu
class MenuTest(TestCase):
    def test_get_item(self):
        item= Menu.objects.create(name='Pizza', price=10)
        self.assertEqual(str(item), 'Pizza : 10')