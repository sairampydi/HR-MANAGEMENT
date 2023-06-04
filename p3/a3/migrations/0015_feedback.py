# Generated by Django 4.2.1 on 2023-06-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a3', '0014_rename_name_salary_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('CommunicationSkills', models.CharField(choices=[('excellent', 'Excellent'), ('good', 'Good'), ('satisfactory', 'Satisfactory'), ('improvement', 'Improvement'), ('below', 'Below')], default='below', max_length=100)),
                ('TeamworkandCollaboration', models.CharField(choices=[('excellent', 'Excellent'), ('good', 'Good'), ('satisfactory', 'Satisfactory'), ('improvement', 'Improvement'), ('below', 'Below')], default='below', max_length=100)),
                ('ProductivityandTimeManagement', models.CharField(choices=[('excellent', 'Excellent'), ('good', 'Good'), ('satisfactory', 'Satisfactory'), ('improvement', 'Improvement'), ('below', 'Below')], default='below', max_length=100)),
                ('ProfessionalismandWorkEthic', models.CharField(choices=[('excellent', 'Excellent'), ('good', 'Good'), ('satisfactory', 'Satisfactory'), ('improvement', 'Improvement'), ('below', 'Below')], default='below', max_length=100)),
                ('JobKnowledgeandSkills', models.CharField(choices=[('excellent', 'Excellent'), ('good', 'Good'), ('satisfactory', 'Satisfactory'), ('improvement', 'Improvement'), ('below', 'Below')], default='below', max_length=100)),
                ('date', models.DateField(blank=True, null=True)),
                ('comments', models.CharField(max_length=100, null=True)),
                ('officername', models.CharField(max_length=20)),
                ('Position', models.CharField(max_length=20)),
            ],
        ),
    ]