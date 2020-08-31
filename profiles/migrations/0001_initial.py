# Generated by Django 3.1 on 2020-08-31 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('default_phone_number', models.CharField(max_length=20)),
                ('default_country', django_countries.fields.CountryField(max_length=2)),
                ('default_postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('default_town_or_city', models.CharField(max_length=40)),
                ('default_street_address1', models.CharField(max_length=80)),
                ('default_street_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('default_county', models.CharField(blank=True, max_length=80, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
