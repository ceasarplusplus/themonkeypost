# Generated by Django 3.1 on 2021-09-09 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210909_0349'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.variants'),
        ),
    ]