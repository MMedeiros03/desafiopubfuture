# Generated by Django 4.0.1 on 2022-01-06 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conta', '0004_conta_numconta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.CharField(max_length=8)),
                ('dataPagamento', models.DateField()),
                ('dataPagamentoEsperado', models.DateField()),
                ('tipoDespesa', models.CharField(choices=[('1', 'alimentacao'), ('2', 'educacao'), ('3', 'lazer'), ('4', 'moradia'), ('5', 'roupa'), ('6', 'saude'), ('7', 'transporte'), ('8', 'outros')], max_length=1)),
                ('conta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='despesas', to='conta.conta')),
            ],
        ),
    ]
