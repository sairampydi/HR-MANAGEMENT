# Generated by Django 4.1.7 on 2023-04-16 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='employee_status',
        ),
        migrations.AddField(
            model_name='user',
            name='date_created',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='user',
            name='employee_id',
            field=models.CharField(default='11', max_length=32, unique=True),
        ),
    ]
