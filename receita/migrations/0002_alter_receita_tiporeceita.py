# Generated by Django 4.0.1 on 2022-01-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='tipoReceita',
            field=models.CharField(choices=[('salario', 'salario'), ('presente', 'presente'), ('premio', 'premio'), ('outros', 'outros')], max_length=8),
        ),
    ]