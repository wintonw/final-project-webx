# Generated by Django 3.1.3 on 2020-11-28 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20201128_0726'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
