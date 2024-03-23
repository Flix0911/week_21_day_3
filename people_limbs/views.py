from .models import People_Limbs
from rest_framework import viewsets, permissions
from .serializer import People_Limbs_Serializer
# Create your views here.

class People_Limbs_View_Set(viewsets.ModelViewSet):
    queryset=People_Limbs.objects.all()
    
    serializer_class=People_Limbs_Serializer
    
    permission_classes=[permissions.AllowAny]
