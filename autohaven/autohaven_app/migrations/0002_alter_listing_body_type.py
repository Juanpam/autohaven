# Generated by Django 5.0.6 on 2024-06-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autohaven_app', '0001_listing_body_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='body_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
