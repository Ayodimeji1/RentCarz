# Generated by Django 5.1.4 on 2024-12-30 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, max_length=15, null=True),
        ),
    ]
