# Generated by Django 4.2 on 2023-09-25 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0003_genome_apollo_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genome',
            name='_metadata',
            field=models.TextField(default='{}'),
        ),
    ]
