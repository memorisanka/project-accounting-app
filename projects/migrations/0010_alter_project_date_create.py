# Generated by Django 4.1.4 on 2023-03-31 16:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_alter_project_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_create',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 31, 18, 33, 32, 406526), verbose_name='Data utworzenia'),
        ),
    ]