# Generated by Django 5.1.4 on 2025-01-21 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_athleteregistration_registratiodate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athleteregistration',
            name='registratioDate',
            field=models.DateField(auto_now=True),
        ),
    ]
