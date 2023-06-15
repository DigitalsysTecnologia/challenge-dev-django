from rest_framework import viewsets
from apps.cadastros.api.serializers import *


class CamposViewSet(viewsets.ModelViewSet):
    queryset = CamposModel.objects.all()
    serializer_class = CamposSerializer


class PropostasViewSet(viewsets.ModelViewSet):
    queryset = PropostasModel.objects.all().order_by('data_registro')
    serializer_class = PropostasSerializer
