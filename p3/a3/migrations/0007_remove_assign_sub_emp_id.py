# Generated by Django 4.2.1 on 2023-06-22 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a3', '0006_syl_updates_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assign_sub',
            name='emp_id',
        ),
    ]