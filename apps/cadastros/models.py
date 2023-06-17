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
        """
        Método que salva o slug do campo.
        """
        if not self.slug or slugify(self.nome) != self.slug:
            self.slug = slugify(self.nome)
        super(CamposModel, self).save(*args, **kwargs)


class PropostasModel(models.Model):
    """
    PropostasModel é a classe que representa as
    propostas que serão cadastradas.
    """

    aprovada = models.BooleanField(default=False)
    data_registro = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Data de registro')
    data_avaliacao = models.DateTimeField(blank=True, null=True,
                                          verbose_name='Data de avaliação')

    class Meta:
        verbose_name = "Proposta"
        verbose_name_plural = "Propostas"
        ordering = ['data_registro']

    @property
    def status(self):
        """
        Método que retorna o status da proposta.
        """
        if self.data_avaliacao is None:
            return 'Aguardando análise'
        else:
            if self.aprovada:
                return 'Aprovada'
            else:
                return 'Reprovada'

    def __str__(self):
        return "{} - {}".format(self.id, self.data_registro.
                                strftime("%d/%m/%Y"))


class RespostasCamposModels(models.Model):
    """
    RespostasCamposModels é a classe que representa as
    respostas dos campos que serão cadastradas.
    """
    proposta = models.ForeignKey(PropostasModel, on_delete=models.CASCADE,
                                 verbose_name='Proposta',
                                 related_name='respostas_proposta')
    campo = models.ForeignKey(CamposModel, on_delete=models.CASCADE,
                              verbose_name='Campo',
                              related_name='respostas_campo')
    resposta = models.CharField(max_length=250, blank=False, null=False,
                                verbose_name='Resposta do campo')

    class Meta:
        verbose_name = "Resposta do campo"
        verbose_name_plural = "Respostas dos campos"
        ordering = ['campo']
