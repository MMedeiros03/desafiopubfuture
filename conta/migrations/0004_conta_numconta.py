# Generated by Django 4.0.1 on 2022-01-06 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0003_alter_conta_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='numConta',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
    ]
