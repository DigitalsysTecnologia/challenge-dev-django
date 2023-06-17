from django.urls import include
from rest_framework.urls import path
from .viewsets import view_campos, view_propostas
urlpatterns = [
    path("propostas", view_propostas),
    path("campos", view_campos),

]
