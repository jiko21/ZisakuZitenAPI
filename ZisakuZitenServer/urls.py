from rest_framework import routers
from .views import GroupViewSet,ZitenViewSet


routers = routers.DefaultRouter()
routers.register('groups',GroupViewSet)
routers.register('ziten',ZitenViewSet)