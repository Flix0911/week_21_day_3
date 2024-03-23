from rest_framework import serializers
from .models import People_Limbs

class People_Limbs_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        Model = People_Limbs
        fields = ('person', 'arm', 'leg', 'feet', 'hands')