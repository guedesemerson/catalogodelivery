# Generated by Django 2.2 on 2020-05-05 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estabelecimento', '0004_estabelecimento_bairro'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='observacao',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]