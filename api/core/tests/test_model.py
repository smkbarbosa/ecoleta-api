from django.test import TestCase
from api.core.models import Point, Item
# Create your tests here.


class PointsTest(TestCase):
    def setUp(self):
        self.obj = Point(
            name='Escola 1',
            lat=-10.1696476,
            long=-48.3474648,
            number='06',
            city='Palmas',
            uf='TO'
        )
        self.obj.save()

    def test_points_exists(self):
        self.assertTrue(Point.objects.exists())

    def test_point_str(self):
        self.assertEqual('Escola 1', str(self.obj))


class ItemTest(TestCase):
    def setUp(self):
        self.obj = Item(
            title='Lampada'
        )

        self.obj.save()
    def test_item_exists(self):
        self.assertTrue(Item.objects.exists())

    def test_item_str(self):
        self.assertEqual('Lampada', str(self.obj))