# Generated by Django 2.1.7 on 2019-03-13 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0007_auto_20190313_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='technology',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='technology_type',
        ),
    ]