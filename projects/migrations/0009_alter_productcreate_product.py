# Generated by Django 4.1.4 on 2023-01-04 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_productcreate_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcreate',
            name='product',
            field=models.ForeignKey(db_column='name', default=None, on_delete=django.db.models.deletion.CASCADE, to='projects.product'),
        ),
    ]
