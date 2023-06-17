from django.contrib import admin
from apps.cadastros.models import CamposModel, PropostasModel, \
    RespostasCamposModels
from apps.cadastros.forms import CamposForm


# Register your models here.


class CamposAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'obrigatorio', 'unico', 'texto_ajuda',
                    'ativo']
    search_fields = ['nome', 'slug', 'obrigatorio', 'unico', 'texto_ajuda',
                     'ativo']
    form = CamposForm


class PropostasAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'data_registro', 'status', 'data_avaliacao']


admin.site.register(CamposModel, CamposAdmin)
admin.site.register(PropostasModel, PropostasAdmin)
admin.site.register(RespostasCamposModels)