# Generated by Django 2.2 on 2020-05-05 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
        ('estabelecimento', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estabelcimento',
            new_name='Estabelecimento',
        ),
    ]