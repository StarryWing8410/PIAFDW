# Generated by Django 3.2.2 on 2021-05-13 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_estanteria_peso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estanteria',
            name='estatura',
            field=models.CharField(max_length=10),
        ),
    ]
