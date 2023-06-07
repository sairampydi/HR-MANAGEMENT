# Generated by Django 4.2.1 on 2023-06-07 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_user_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(choices=[('hod', 'Hod'), ('employee', 'Employee')], default='none', max_length=30),
        ),
    ]
