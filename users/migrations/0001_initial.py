# Generated by Django 5.1.4 on 2025-01-06 11:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, max_length=100, null=True)),
                ('lastName', models.CharField(blank=True, max_length=100, null=True)),
                ('eMail', models.EmailField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('mobNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('altMobNumber', models.CharField(blank=True, max_length=15, null=True)),
                ('addressLine1', models.TextField(blank=True, null=True)),
                ('addressLine2', models.TextField(blank=True, null=True)),
                ('pin', models.CharField(blank=True, max_length=15, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('school', models.CharField(blank=True, max_length=100, null=True)),
                ('academy', models.CharField(blank=True, max_length=100, null=True)),
                ('aadhar', models.CharField(blank=True, max_length=100, null=True)),
                ('sport', models.CharField(blank=True, max_length=100, null=True)),
                ('height', models.CharField(blank=True, max_length=100, null=True)),
                ('weight', models.CharField(blank=True, max_length=100, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
