# Generated by Django 3.2.8 on 2022-01-06 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0027_auto_20211108_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='active_concepts',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='active_mappings',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]