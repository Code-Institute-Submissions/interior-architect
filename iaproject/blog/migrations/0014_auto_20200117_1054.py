# Generated by Django 2.2.9 on 2020-01-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20200117_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='order',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
