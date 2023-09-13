# Generated by Django 4.1 on 2023-07-29 01:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_fotografia_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('raca', models.CharField(max_length=150)),
                ('categoria', models.CharField(choices=[('GATO', 'Gato'), ('CACHORRO', 'Cachorro'), ('PÁSSAROS', 'Pássaros'), ('OUTROS', 'Outros')], default='', max_length=100)),
                ('idade', models.PositiveIntegerField(max_length=10)),
                ('cor', models.CharField(max_length=20)),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')),
                ('publicada', models.BooleanField(default=False)),
                ('data_cadastro', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Fotografia',
        ),
    ]