# Generated by Django 4.0.4 on 2022-06-04 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoplanner_app', '0002_remove_coordinates_id_coordinates_coordinate_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coordinates',
            name='coordinate_order',
        ),
        migrations.AddField(
            model_name='coordinates',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
