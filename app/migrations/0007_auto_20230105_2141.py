# Generated by Django 3.2.16 on 2023-01-05 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_jointventure'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jointventure',
            name='closing_date',
        ),
        migrations.RemoveField(
            model_name='jointventure',
            name='date_aggreement',
        ),
        migrations.RemoveField(
            model_name='jointventure',
            name='inspection_date',
        ),
    ]
