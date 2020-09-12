from django.test import TestCase

from users.models import CustomUser

from .models import Item


class ItemTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user
        test_user = CustomUser.objects.create_user(
            email='test@test.com',
            username='test_user',
            password='test123456')
        test_user.save()

        # Create an Item
        test_item = Item.objects.create(
            name='test item',
            price=125,
            size='M',
            color='Yellow',
            created_by=test_user)
        test_item.save()

    def test_item_content(self):
        item = Item.objects.last()
        actual_name = f'{item.name}'
        actual_price = f'{item.price}'
        actual_size = f'{item.size}'
        actual_color = f'{item.color}'
        actual_created_by = f'{item.created_by}'
        self.assertEqual(actual_name, 'test item')
        self.assertEqual(actual_price, '125.00')
        self.assertEqual(actual_size, 'M')
        self.assertEqual(actual_color, 'Yellow')
        self.assertEqual(actual_created_by, 'test@test.com')
