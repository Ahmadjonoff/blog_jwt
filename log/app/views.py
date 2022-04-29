from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

class MuallifViewSet(ModelViewSet):
    queryset = Muallif.objects.all()
    serializer_class = MuallifSer
    permission_classes = [IsAuthenticated, ]

class TalksViewSet(ModelViewSet):
    queryset = Talks.objects.all()
    serializer_class = TalksSer
    permission_classes = [IsAuthenticated, ]

class MaqolaViewSet(ModelViewSet):
    queryset = Maqola.objects.all()
    serializer_class = MaqolaSer
    permission_classes = [IsAuthenticated, ]