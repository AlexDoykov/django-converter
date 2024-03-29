# Generated by Django 2.2.3 on 2019-08-02 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0013_auto_20190617_2107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currency',
            name='exchange_rate',
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=7, max_digits=10)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='converter.Currency')),
            ],
        ),
    ]
