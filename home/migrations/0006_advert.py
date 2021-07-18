# Generated by Django 3.1 on 2021-07-18 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20210713_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('advert', models.ImageField(blank=True, upload_to='images/breadcrumb/')),
                ('news', models.BooleanField(default=False)),
                ('store', models.BooleanField(default=False)),
                ('audio', models.BooleanField(default=False)),
                ('video', models.BooleanField(default=False)),
                ('account', models.BooleanField(default=False)),
            ],
        ),
    ]
