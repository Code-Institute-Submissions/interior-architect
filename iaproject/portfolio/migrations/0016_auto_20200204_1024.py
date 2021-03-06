# Generated by Django 2.2.9 on 2020-02-04 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_project_pdf_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='project',
            name='pdf_price',
        ),
        migrations.CreateModel(
            name='Download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500)),
                ('content', models.TextField()),
                ('download', models.FileField(upload_to='project_downloads')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('exclude', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='downloads', to='portfolio.Project')),
            ],
        ),
    ]
