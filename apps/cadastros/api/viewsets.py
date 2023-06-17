from rest_framework import viewsets
from apps.cadastros.api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def view_campos(request):
    qs = CamposModel.objects.all()
    serializer = CamposSerializer(qs, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def view_propostas(request):
    if request.method == 'GET':
        qs = PropostasModel.objects.all()
        if qs.count() == 0:
            content = {'Sua requisição foi atendida com sucesso, no entanto, '
                       'não há registros a serem exibidos.'}
            return Response(content, status=status.HTTP_204_NO_CONTENT)
        serializer = PropostasSerializer(qs, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PropostasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            proposta_atual = PropostasModel.objects.latest('pk')
            dict_respostas = request.data
            """
            O dicionário dict_respostas é um dicionário que contém os valores 
            inseridos no formulário e enviados  pela a API atavés do POST.
            Nesse momento, ele percorre o dicionário e cria um registros para
            cada resposta
            """
            for valor in dict_respostas:

                RespostasCamposModels.objects.create(
                    proposta_id=proposta_atual.id,
                    campo=CamposModel.objects.get(slug__exact=valor),
                    resposta=dict_respostas[valor]
                )

            content = {'Sua requisição foi atendida com sucesso.'}
            return Response(content, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    else:
        content = {'Sua requisição não pode ser atendida.'}
        return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)


