# Generated by Django 3.0.5 on 2020-04-13 12:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
