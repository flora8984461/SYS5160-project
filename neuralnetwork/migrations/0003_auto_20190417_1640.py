# Generated by Django 2.1.5 on 2019-04-17 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neuralnetwork', '0002_auto_20190417_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weights',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
