# Generated by Django 5.1.4 on 2024-12-21 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viviendas', '0002_alter_vivienda_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vivienda',
            name='foto',
        ),
        migrations.AddField(
            model_name='vivienda',
            name='foto_url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]