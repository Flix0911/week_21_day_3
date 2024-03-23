from .models import People
from rest_framework import serializers

# create serializer class
class People_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=People
        fields=('id', 'first_name', 'middle_name', 'last_name', 'country_of_origin', 'ssn', 'age')