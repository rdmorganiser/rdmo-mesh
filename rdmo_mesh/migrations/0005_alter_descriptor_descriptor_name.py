# Generated by Django 3.2.6 on 2021-10-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rdmo_mesh', '0004_add_gin_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='descriptor',
            name='descriptor_name',
            field=models.CharField(max_length=256),
        ),
    ]
