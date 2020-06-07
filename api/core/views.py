from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.core.models import Item, Point
from api.core.serializers import ItemSerializer, PointSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_item(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except Item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # busca item
    if request.method == 'GET':
        serializer = ItemSerializer(item)
        return Response(serializer.data)
    #deleta item
    elif request.method == 'DELETE':
        return Response({})
    #atualiza item
    elif request.method == 'PUT':
        return Response({})


@api_view(['GET', 'POST'])
def get_post_item(request):
    import ipdb
    # busca todos
    if request.method == 'GET':
        itens = Item.objects.all()
        serializer = ItemSerializer(itens, many=True)
        return Response(serializer.data)
    # insere um novo item
    if request.method == 'POST':
        ipdb.set_trace()
        data = {
            'title': request.data.get('title'),
            'points': request.data.get('points')
        }
        serializer = ItemSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class PointViewSet(viewsets.ModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
