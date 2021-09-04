# Generated by Django 2.2.24 on 2021-09-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210901_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_admin',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_staff',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_superuser',
            field=models.BooleanField(default=False, null=True),
        ),
    ]