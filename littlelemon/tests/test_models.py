from django.test import TestCase

from restaurant.models import MenuItem, Booking

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(f'{item.title} : {item.price}', 'IceCream : 80')

class BookingTest(TestCase):
    def test_get_item(self):
        item = Booking.objects.create(name='Visitor1', no_of_guests=80)
        self.assertEqual(f'{item.name} : {item.no_of_guests}', 'Visitor1 : 80')