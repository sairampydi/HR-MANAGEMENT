# Generated by Django 4.1.7 on 2023-04-17 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_employee_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date_created',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
