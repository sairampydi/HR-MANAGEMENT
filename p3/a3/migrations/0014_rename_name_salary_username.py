# Generated by Django 4.2 on 2023-05-11 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a3', '0013_salary_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salary',
            old_name='name',
            new_name='username',
        ),
    ]
