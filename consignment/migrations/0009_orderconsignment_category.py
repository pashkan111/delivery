# Generated by Django 2.2.24 on 2021-08-31 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0008_auto_20210830_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderconsignment',
            name='category',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default=1, max_length=20),
        ),
    ]