# Generated by Django 4.1.4 on 2023-01-26 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_date_create'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ServiceCreate',
            new_name='ServiceForProject',
        ),
    ]
