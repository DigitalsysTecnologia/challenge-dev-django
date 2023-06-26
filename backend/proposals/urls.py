from django.urls import path

from proposals import views

urlpatterns = [
    path(
        '',
        views.proposals_list,
        name='proposals_list'
    ),
    path(
        'celery',
        views.proposals_list_celery,
        name='proposals_list_celery'
    ),
    path(
        '<int:pk>',
        views.proposal_detail,
        name='proposal_detail'
    ),
]
