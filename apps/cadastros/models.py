from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator


# Create your models here.


class CamposModel(models.Model):
    """
    CamposModel é a classe que representa os campos que poderão ser utilizados
    no cadastro de propostas.
    """
    nome = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, editable=False, blank=True,
                            null=False)
    texto_ajuda = models.CharField(max_length=200, blank=True, null=True)
    unico = models.BooleanField(default=False,
                                verbose_name="Campo único")
    obrigatorio = models.BooleanField(default=False,
                                      verbose_name="Campo obrigatório")
    ativo = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Campo"
        verbose_name_plural = "Campos"
        ordering = ['nome']

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        # Função responsável por criar o slug do campo
        self.slug = slugify(self.nome)
        super(CamposModel, self).save(*args, **kwargs)


class PropostasModel(models.Model):
    """
    PropostasModel é a classe que representa as
    propostas que serão cadastradas.
    """
    campos = models.ManyToManyField(CamposModel, verbose_name='Campos',
                                    related_name='campos_proposta')
    valor = models.DecimalField(max_digits=13, decimal_places=2,
                                validators=[MinValueValidator(0.00)],
                                verbose_name='Valor da proposta',
                                blank=False, null=False)
    ativa = models.BooleanField(default=True)
    aprovada = models.BooleanField(default=False)
    data_registro = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Data de registro')
    data_avaliacao = models.DateTimeField(blank=True, null=True,
                                          verbose_name='Data de avaliação')

    class Meta:
        verbose_name = "Proposta"
        verbose_name_plural = "Propostas"
        ordering = ['data_registro']