# Generated by Django 2.2.2 on 2019-06-14 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0006_auto_20190614_0607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='exchange_rate',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
