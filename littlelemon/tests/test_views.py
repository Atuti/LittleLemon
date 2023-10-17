from django.test import TestCase

from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title='IceCream', price=80, inventory=100)

    def test_menu_view_data(self):
        item = MenuItem.objects.get(id=1)
        self.assertEqual(item.title, 'IceCream')