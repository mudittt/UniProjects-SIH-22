# Generated by Django 4.0.2 on 2022-03-18 17:42

import backend.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_alter_project_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='members',
            field=models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='university',
            name='logo',
            field=models.ImageField(upload_to=backend.models.upload_to),
        ),
    ]