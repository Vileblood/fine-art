# Generated by Django 3.1 on 2020-08-17 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_painting_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='year',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
