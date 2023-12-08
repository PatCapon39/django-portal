# Generated by Django 4.2 on 2023-12-08 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0012_alter_genome_ncbi_bioproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genome',
            name='_metadata_yaml',
            field=models.TextField(blank=True, help_text='Metadata in YAML format. Should be one `key: value` pair per line.', null=True),
        ),
        migrations.AlterField(
            model_name='genome',
            name='apollo_url',
            field=models.URLField(blank=True, help_text='URL pointing to a public Apollo genome/tracks.', null=True),
        ),
        migrations.AlterField(
            model_name='genome',
            name='condition',
            field=models.CharField(blank=True, help_text='e.g. chemical exposure, genetic manipulation, cancer.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='genome',
            name='description_html',
            field=models.TextField(blank=True, help_text='Description of the genome with inline HTML. Use `<br>` for a new line and `<a>` tags for links.', null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='apollo_url',
            field=models.URLField(blank=True, help_text='URL pointing to an Apollo login page.', null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='description_html',
            field=models.TextField(blank=True, help_text='Description of the genome with inline HTML. Use `<br>` for a new line and `<a>` tags for links.', null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='email',
            field=models.EmailField(blank=True, help_text='Contact email address, if consent has been given to show.', max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='website_url',
            field=models.URLField(blank=True, help_text='URL pointing to lab group public website.', null=True),
        ),
    ]
