# Generated by Django 4.2.1 on 2023-06-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a3', '0008_alter_profile_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile(d).png', upload_to='account/images'),
        ),
    ]