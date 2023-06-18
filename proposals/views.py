# Create your views here.
from celery import shared_task
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from proposals.serializer import ProposalSerializer
from proposals.models import Proposal


@shared_task()
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
        proposal = create_proposal.delay(request.data)
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
