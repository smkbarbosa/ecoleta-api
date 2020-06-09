import json

from model_mommy import mommy
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.test import APIClient

from api.core.models import Item, Point
from api.core.serializers import ItemSerializer

client = APIClient()


class GetAllItensTest(TestCase):
    def setUp(self):
        Item.objects.create(
            title='Lampada'
        )
        Item.objects.create(
            title='Papelão'
        )
        Item.objects.create(title='Lata')

    def test_get_all_itens(self):

        #GET
        response = client.get(reverse('get_post_item'))
        #get from db
        itens = Item.objects.all()
        serializer = ItemSerializer(itens, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleItemTest(TestCase):
    def setUp(self):
        self.lampada = Item(title='Lampada')
        self.lampada.save()
        self.papelao = Item(title='Papelão')
        self.papelao.save()
        self.lata = Item(title='Lata')
        self.lata.save()

    def test_get_valid_single_item(self):
        client.login(username='samuel', password='123456')
        response = client.get(reverse('get_delete_update_item', kwargs={'pk': self.lata.pk}))
        item = Item.objects.get(pk=self.lata.pk)
        serializer = ItemSerializer(item)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_item(self):
        response = client.get(reverse('get_delete_update_item', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewItemTest(TestCase):
    def setUp(self):
        self.item = mommy.make(Item, _fill_optional=True, point__name='escola 1')
        self.item.save()

        self.valid_payload = self.item.__dict__
        self.invalid_payload = {
            'title': ''
        }

    def test_create_valid_item(self):

        response = client.post(
            reverse('item-list'),
            data=self.valid_payload,
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_item(self):
        client.login(username='samuel', password='123456')
        response = client.post(
            reverse('item-list'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
