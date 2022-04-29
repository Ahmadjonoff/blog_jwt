from rest_framework.serializers import ModelSerializer
from .models import *

class MuallifSer(ModelSerializer):
    class Meta:
        model = Muallif
        fields = "__all__"

class MaqolaSer(ModelSerializer):
    class Meta:
        model = Maqola
        fields = "__all__"

class TalksSer(ModelSerializer):
    class Meta:
        model = Talks
        fields = "__all__"