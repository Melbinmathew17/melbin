# Generated by Django 4.1.7 on 2023-04-08 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='positiondb',
            name='age',
        ),
        migrations.AddField(
            model_name='positiondb',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
