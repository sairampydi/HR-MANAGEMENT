# Generated by Django 4.2.1 on 2023-06-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a3', '0017_profile_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assign_sub',
            name='section',
            field=models.IntegerField(default=0),
        ),
    ]