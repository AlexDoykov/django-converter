# Generated by Django 2.2.4 on 2019-08-07 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0017_auto_20190807_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='valid_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='valid date'),
        ),
    ]