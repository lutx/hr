# Generated by Django 2.1.7 on 2019-03-12 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee_tech',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Employee', unique=True),
        ),
    ]
