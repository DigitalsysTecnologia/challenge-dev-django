from django.contrib import admin
from apps.cadastros.models import CamposModel, PropostasModel
from apps.cadastros.forms import CamposForm, PropostasForm


# Register your models here.


class CamposAdmin(admin.ModelAdmin):
    list_display = ['nome', 'slug', 'obrigatorio', 'unico', 'texto_ajuda',
                    'ativo']
    search_fields = ['nome', 'slug', 'obrigatorio', 'unico', 'texto_ajuda',
                     'ativo']
    form = CamposForm


class PropostasAdmin(admin.ModelAdmin):

    form = PropostasForm


admin.site.register(CamposModel, CamposAdmin)
admin.site.register(PropostasModel, PropostasAdmin)
