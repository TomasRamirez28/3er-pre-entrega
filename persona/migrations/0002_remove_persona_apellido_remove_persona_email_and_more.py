# Generated by Django 5.0.6 on 2024-06-20 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='apellido',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='email',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='fecha_nacimiento',
        ),
    ]