# Generated by Django 3.2.8 on 2021-11-01 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0014_remove_renttable_wallet'),
    ]

    operations = [
        migrations.AddField(
            model_name='renttable',
            name='wallet_amount',
            field=models.FloatField(null=True),
        ),
    ]
