# Generated by Django 5.1.4 on 2025-01-21 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='athleteregistration',
            name='registratioDate',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
    ]
