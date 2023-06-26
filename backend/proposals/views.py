# Create your views here.
import json
import pdb

from celery import shared_task
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_celery_results.models import TaskResult

from proposals.models import Proposal
from proposals.serializers import ProposalSerializer


@shared_task()
def create_proposal_celery(data):
    serializer = ProposalSerializer(data=data)

    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


def create_proposal(data):
    serializer = ProposalSerializer(data=data)

    serializer.is_valid(raise_exception=True)
    serializer.save()
    return serializer.data


@api_view(['get', 'post'])
def proposals_list(request):
    if request.method == 'GET':
        proposals = Proposal.objects.all()
        serializer = ProposalSerializer(
            instance=proposals,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
    if request.method == 'POST':
        proposal = create_proposal(request.data)
        return Response(
            {'proposal': proposal},
            status=status.HTTP_201_CREATED
        )


@api_view(['get', 'post'])
def proposals_list_celery(request):
    if request.method == 'GET':
        queue_object_results = TaskResult.objects.all()

        lista = []
        for _obj in queue_object_results:
            if _obj.result:
                lista.append({
                    "status": _obj.status,
                    "result": json.loads(_obj.result)
                })

        if queue_object_results:
            return Response(lista)
        else:
            return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        data = {
            "value": request.data['value'],
            "user": request.data['user']
        }
        print(data)
        proposal = create_proposal_celery.delay(data)
        return Response(
            {'proposal': proposal.id},
            status=status.HTTP_201_CREATED
        )


@api_view()
def proposal_detail(request, pk):
    proposal = Proposal.objects.filter(pk=pk).first()
    if proposal:
        serializer = ProposalSerializer(
            instance=proposal,
            many=False,
            context={'request': request}
        )
        return Response(serializer.data)
    else:
        return Response({"detail": "Not Found"}, status=status.HTTP_404_NOT_FOUND)
