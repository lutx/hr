# Generated by Django 2.1.7 on 2019-03-13 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0006_auto_20190313_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technology_type',
            name='technology',
        ),
        migrations.RemoveField(
            model_name='employee_tech',
            name='technology',
        ),
        migrations.AddField(
            model_name='employee_tech',
            name='technology',
            field=models.ManyToManyField(to='hr.Technology'),
        ),
        migrations.RemoveField(
            model_name='employee_tech',
            name='technology_type',
        ),
        migrations.AddField(
            model_name='employee_tech',
            name='technology_type',
            field=models.ManyToManyField(to='hr.Technology_type'),
        ),
    ]
