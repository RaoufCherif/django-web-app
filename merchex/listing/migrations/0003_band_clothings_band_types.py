# Generated by Django 4.1.7 on 2023-03-02 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='clothings',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='types',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
