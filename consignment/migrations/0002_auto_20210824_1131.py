# Generated by Django 2.2.24 on 2021-08-24 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderconsignment',
            name='phone_entity',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Контактный телефон'),
        ),
        migrations.AlterField(
            model_name='orderconsignment',
            name='phone_individual',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Контактный телефон'),
        ),
    ]