# Generated by Django 3.1 on 2021-07-13 09:04

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_nextmatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='donate',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
