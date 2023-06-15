from django.urls import include
from rest_framework.urls import path
from .viewsets import CamposViewSet, PropostasViewSet
urlpatterns = [
    path("", PropostasViewSet.as_view({"get": "list"})),
    path("campos", CamposViewSet.as_view({"get": "list"})),
]