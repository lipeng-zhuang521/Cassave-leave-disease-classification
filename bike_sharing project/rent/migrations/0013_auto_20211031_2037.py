# Generated by Django 3.2.8 on 2021-10-31 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0012_auto_20211031_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='renttable',
            name='charges',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='renttable',
            name='wallet',
            field=models.FloatField(null=True),
        ),
    ]
