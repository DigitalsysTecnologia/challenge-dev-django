from apps.cadastros.models import PropostasModel, CamposModel, \
    RespostasCamposModels
from rest_framework import serializers


class CamposSerializer(serializers.ModelSerializer):
    class Meta:
        model = CamposModel
        fields = '__all__'


class CamposRespostasSerialzer(serializers.ModelSerializer):
    class Meta:
        model = RespostasCamposModels


class RespostaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespostasCamposModels
        fields = '__all__'


class PropostasSerializer(serializers.ModelSerializer):
    respostas = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    data_registro = serializers.SerializerMethodField()

    def get_status(self, obj):
        return str(obj.status)

    def get_data_registro(self, obj):
        return obj.data_registro.strftime("%d/%m/%Y"
                                          + " às "
                                          + "%H:%M:%S")

    def get_respostas(self, obj):
        qs = obj.respostas_proposta.all()
        return RespostaModelSerializer(qs, many=True).data

    class Meta:
        model = PropostasModel
        fields = ['__str__', 'respostas', 'status',
                  'data_avaliacao', 'data_registro']
