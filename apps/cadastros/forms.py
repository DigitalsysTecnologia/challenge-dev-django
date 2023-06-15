from django import forms
from apps.cadastros.models import CamposModel, PropostasModel


class CamposForm(forms.ModelForm):
    class Meta:
        model = CamposModel
        fields = '__all__'

    def clean(self):
        # Verifica se o campo nome já existe  na base de dados
        data = self.cleaned_data
        if CamposModel.objects.filter(nome=data['nome']).exists():
            raise forms.ValidationError("Um campo com o nome "
                                        "{} já existe.".format(data['nome']))


class PropostasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PropostasForm, self).__init__()
        # Adiciona os campos no formulário
        for campo in CamposModel.objects.filter(ativo=True):
            checar_obrigatoriedade = campo.obrigatorio
            self.fields[campo.nome] = forms.CharField(
                label=campo.nome,
                required=checar_obrigatoriedade,
                widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = PropostasModel
        fields = '__all__'
