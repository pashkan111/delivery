# Generated by Django 2.2.24 on 2021-09-02 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210901_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='username',
        ),
    ]