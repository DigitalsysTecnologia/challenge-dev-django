from apps.cadastros.models import PropostasModel, CamposModel
from rest_framework import serializers


class CamposSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamposModel
        fields = '__all__'


class PropostasSerializer(serializers.ModelSerializer):
    campos = CamposSerializer(read_only=True, many=True)

    class Meta:
        model = PropostasModel
        fields = '__all__'
