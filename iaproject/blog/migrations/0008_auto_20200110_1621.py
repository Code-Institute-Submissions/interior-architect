# Generated by Django 2.2.9 on 2020-01-10 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_bullet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='section',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
