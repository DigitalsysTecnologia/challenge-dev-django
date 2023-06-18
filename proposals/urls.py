from django.urls import path

from proposals import views

urlpatterns = [
    path(
        'proposals',
        views.proposals_list,
        name='proposals_list'
    ),
    path(
        'proposals/<int:pk>',
        views.proposal_detail,
        name='proposal_detail'
    ),
    path(
        'proposal',
        views.create_proposal,
        name='create_proposal'
    ),
]
