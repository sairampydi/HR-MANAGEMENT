# Generated by Django 4.2.1 on 2023-07-07 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a3', '0017_profile_name_alter_profile_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stream',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
