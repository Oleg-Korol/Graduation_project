# Generated by Django 3.2.15 on 2023-01-12 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_record_client_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='time_servise',
            field=models.DateField(default='2023-01-01', verbose_name='День  ТО'),
            preserve_default=False,
        ),
    ]
