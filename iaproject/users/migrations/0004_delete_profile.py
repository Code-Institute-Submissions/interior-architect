# Generated by Django 2.2.10 on 2020-02-13 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200122_1030'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]