# Generated by Django 2.1.4 on 2020-02-28 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200228_1018'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='ls_active',
            new_name='is_active',
        ),
    ]
