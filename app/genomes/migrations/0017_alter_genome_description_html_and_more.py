# Generated by Django 4.2 on 2024-08-17 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genomes', '0016_alter_track_track_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genome',
            name='description_html',
            field=models.TextField(blank=True, help_text='Description of the genome with inline HTML. Use `&lt;br&gt;` for a new line and `&lt;a&gt;` tags for links.', null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='description_html',
            field=models.TextField(blank=True, help_text='Description of the genome with inline HTML. Use `&lt;br&gt;` for a new line and `&lt;a&gt;` tags for links.', null=True),
        ),
        migrations.AlterField(
            model_name='track',
            name='description_html',
            field=models.TextField(blank=True, help_text='Description of the genome with inline HTML. Use `&lt;br&gt;` for a new line and `&lt;a&gt;` tags for links.', null=True),
        ),
    ]
