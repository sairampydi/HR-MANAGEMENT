# Generated by Django 4.2.1 on 2023-06-07 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a3', '0018_alter_assign_sub_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='position',
        ),
    ]