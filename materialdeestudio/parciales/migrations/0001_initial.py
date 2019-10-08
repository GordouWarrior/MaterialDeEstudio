# Generated by Django 2.2.6 on 2019-10-08 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaterialDeEstudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.CharField(max_length=15)),
                ('profesor', models.CharField(max_length=15)),
                ('semestre', models.CharField(max_length=15)),
                ('fecha', models.DateTimeField(max_length=15)),
                ('archivo', models.FileField(upload_to='images/')),
                ('imagen', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('clave', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=20)),
                ('sede', models.CharField(max_length=30)),
            ],
        ),
    ]
