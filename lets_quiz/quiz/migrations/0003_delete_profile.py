# Generated by Django 5.1.2 on 2024-10-30 03:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]