# Generated by Django 4.2.4 on 2023-09-06 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
