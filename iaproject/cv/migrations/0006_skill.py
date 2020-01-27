# Generated by Django 2.2.9 on 2020-01-27 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20200127_1230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program', models.CharField(max_length=50)),
                ('percent', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
    ]
