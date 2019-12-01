from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Ziten,Group
from .serializer import ZitenSerializer,GroupSerializer
# Create your views here.


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ZitenViewSet(viewsets.ModelViewSet):
    queryset = Ziten.objects.all()
    serializer_class = ZitenSerializer