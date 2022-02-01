# Generated by Django 3.2.9 on 2022-02-01 22:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20220201_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.AddField(
            model_name='category',
            name='cat_options',
            field=models.CharField(blank=True, choices=[('games', 'GAMES'), ('consoles', 'CONSOLES'), ('accessories', 'ACCESSORIES')], max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('discount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('active', models.BooleanField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]