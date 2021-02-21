# Generated by Django 3.1.6 on 2021-02-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JarColour', models.CharField(max_length=254)),
                ('ScentOne', models.CharField(max_length=254)),
                ('ScentTwo', models.CharField(max_length=254)),
                ('quantity', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('items', models.ManyToManyField(blank=True, null=True, to='bag.CartItem')),
            ],
        ),
    ]
