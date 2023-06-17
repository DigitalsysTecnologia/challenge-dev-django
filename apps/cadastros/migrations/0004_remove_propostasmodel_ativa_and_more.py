# Generated by Django 4.2.2 on 2023-06-17 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("cadastros", "0003_remove_propostasmodel_campos_propostasmodel_campos"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="propostasmodel",
            name="ativa",
        ),
        migrations.RemoveField(
            model_name="propostasmodel",
            name="valor",
        ),
        migrations.CreateModel(
            name="RespostasCamposModels",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "resposta",
                    models.CharField(max_length=250, verbose_name="Resposta do campo"),
                ),
                (
                    "campo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="respostas_campo",
                        to="cadastros.camposmodel",
                        verbose_name="Campo",
                    ),
                ),
                (
                    "proposta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="respostas_proposta",
                        to="cadastros.propostasmodel",
                        verbose_name="Proposta",
                    ),
                ),
            ],
            options={
                "verbose_name": "Resposta do campo",
                "verbose_name_plural": "Respostas dos campos",
                "ordering": ["campo"],
            },
        ),
    ]
