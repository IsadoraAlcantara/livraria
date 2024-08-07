# Generated by Django 5.0.2 on 2024-07-30 12:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_autor_options_livro_categoria"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="eidtora",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="livros",
                to="core.editora",
            ),
        ),
        migrations.AlterField(
            model_name="livro",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="livros",
                to="core.categoria",
            ),
        ),
    ]
