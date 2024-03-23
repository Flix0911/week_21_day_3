from .models import People
from rest_framework import viewsets, permissions
from .serializer import People_Serializer

# create view class
class People_View_Set(viewsets.ModelViewSet):
    queryset=People.objects.all().order_by('id')
    
    serializer_class=People_Serializer
    
    permission_classes=[permissions.AllowAny]