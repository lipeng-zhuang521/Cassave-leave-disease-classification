# Generated by Django 3.2.8 on 2021-10-31 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20211031_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
    ]
