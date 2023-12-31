# Generated by Django 4.1 on 2023-07-29 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('telefone', models.IntegerField(max_length=100)),
                ('endereco', models.CharField(max_length=250)),
            ],
        ),
    ]
