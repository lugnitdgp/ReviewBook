# Generated by Django 3.0 on 2020-02-01 06:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_auto_20200123_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamereview',
            name='rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
