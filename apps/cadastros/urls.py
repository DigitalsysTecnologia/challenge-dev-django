from django.urls import path
from apps.cadastros.views import CadastrarPropostaView

urlpatterns = [
    path('', CadastrarPropostaView.as_view(), name='cadastros'),
]