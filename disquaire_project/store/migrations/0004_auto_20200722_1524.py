# Generated by Django 3.0.8 on 2020-07-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20200722_1511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='artists',
        ),
        migrations.AddField(
            model_name='album',
            name='artists',
            field=models.ManyToManyField(blank=True, related_name='albums', to='store.Artist'),
        ),
    ]
