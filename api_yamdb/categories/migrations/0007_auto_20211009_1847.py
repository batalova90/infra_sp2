# Generated by Django 2.2.16 on 2021-10-09 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_merge_20211008_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['id'], 'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='titles',
            options={'ordering': ['id'], 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
    ]