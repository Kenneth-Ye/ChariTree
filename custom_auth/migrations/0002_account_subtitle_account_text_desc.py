# Generated by Django 4.2.13 on 2024-05-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='text_desc',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
