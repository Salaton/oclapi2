# Generated by Django 3.2.7 on 2021-09-14 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0017_auto_20210720_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concept',
            name='internal_reference_id',
        ),
        migrations.RemoveField(
            model_name='localizedtext',
            name='internal_reference_id',
        ),
    ]
