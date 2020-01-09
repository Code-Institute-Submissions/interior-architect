# Generated by Django 2.2.9 on 2020-01-09 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examples', to='portfolio.Project')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='examples', to='cv.Role')),
            ],
        ),
    ]
