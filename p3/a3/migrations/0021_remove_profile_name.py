# Generated by Django 4.2.1 on 2023-07-07 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a3', '0020_remove_profile_stream'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]