# Generated by Django 4.1 on 2023-07-29 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Tutor', '0001_initial'),
        ('galeria', '0006_pet_delete_fotografia'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='tutor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Tutor.tutor'),
        ),
    ]