# Generated by Django 2.2.9 on 2020-01-22 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20200122_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='caption',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='caption_url',
        ),
    ]
