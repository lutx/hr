# Generated by Django 2.1.5 on 2019-03-14 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0009_auto_20190313_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_tech',
            name='technology',
        ),
        migrations.AddField(
            model_name='employee_tech',
            name='technology',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='hr.Technology'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='employee_tech',
            name='technology_type',
        ),
        migrations.AddField(
            model_name='employee_tech',
            name='technology_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hr.Technology_type'),
            preserve_default=False,
        ),
    ]
