from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from . import views
from .views import ItemViewSet, PointViewSet

api_router = routers.DefaultRouter()
api_router.register(r'item', ItemViewSet)
api_router.register(r'point', PointViewSet)

urlpatterns = [
    path("api/v1/", include(api_router.urls)),
    url('^api/v1/item/(?P<pk>[0-9]+)$', views.get_delete_update_item, name='get_delete_update_item'),
    url('^api/v1/item/$', views.get_post_item, name='get_post_item')

]
