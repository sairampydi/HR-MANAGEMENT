# Generated by Django 4.2.1 on 2023-07-07 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a3', '0022_profile_deaprtment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='deaprtment',
            new_name='department',
        ),
    ]
