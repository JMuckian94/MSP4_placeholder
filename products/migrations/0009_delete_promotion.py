# Generated by Django 3.2.9 on 2022-02-02 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_auto_20220202_2016'),
        ('products', '0008_auto_20220202_1948'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Promotion',
        ),
    ]
