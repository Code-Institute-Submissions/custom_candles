# Generated by Django 3.1.6 on 2021-02-21 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='colours',
            options={'verbose_name_plural': 'Colours'},
        ),
        migrations.AlterModelOptions(
            name='scents',
            options={'verbose_name_plural': 'Scents'},
        ),
    ]
