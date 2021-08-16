# Generated by Django 2.2.24 on 2021-08-16 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_standart_to', models.CharField(max_length=255)),
                ('term_standart_from', models.CharField(max_length=255)),
                ('term_express_to', models.CharField(max_length=255)),
                ('term_express_from', models.CharField(max_length=255)),
                ('cityfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='term_cityfrom', to='calculator.City')),
                ('cityto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='term_cityto', to='calculator.City')),
            ],
        ),
        migrations.CreateModel(
            name='Calculate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weightto', models.CharField(max_length=255)),
                ('weightfrom', models.CharField(max_length=255)),
                ('inter_terminal', models.CharField(max_length=255)),
                ('pickup', models.CharField(max_length=255)),
                ('cityfrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calc_cityfrom', to='calculator.City')),
                ('cityto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calc_cityto', to='calculator.City')),
            ],
        ),
    ]