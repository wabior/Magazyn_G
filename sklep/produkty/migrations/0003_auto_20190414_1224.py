# Generated by Django 2.2 on 2019-04-14 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0002_auto_20190414_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produkt',
            name='opis',
            field=models.TextField(blank=True),
        ),
    ]
