# Generated by Django 2.2 on 2020-05-14 15:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sugestao', '0004_auto_20200513_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sugestao',
            name='data_insercao',
            field=models.DateField(default=datetime.date(2020, 5, 14)),
        ),
    ]
