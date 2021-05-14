# Generated by Django 3.2.2 on 2021-05-13 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=1)),
                ('material', models.CharField(max_length=20)),
                ('peso', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Locker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('puertas', models.CharField(max_length=1)),
                ('material', models.CharField(max_length=20)),
                ('tipo', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=10)),
                ('precio', models.CharField(max_length=20)),
                ('dimensiones', models.CharField(max_length=20)),
            ],
        ),
    ]
