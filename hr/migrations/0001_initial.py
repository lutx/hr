# Generated by Django 2.1.7 on 2019-03-11 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('work_experience', models.IntegerField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/emp/')),
            ],
        ),
        migrations.CreateModel(
            name='Employee_tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skil_level', models.CharField(choices=[('Junior', 'Junior'), ('Mid', 'Mid'), ('Senior', 'Senior')], max_length=30)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('PHP', 'PHP'), ('Python', 'Python'), ('JavaScript', 'JavaScript'), ('C#', 'C#'), ('Java', 'Java'), ('C', 'C'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('SQL', 'SQL'), ('TypeScript', 'TypeScript'), ('Ruby', 'Ruby')], max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/technology/')),
            ],
        ),
        migrations.CreateModel(
            name='Technology_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='technology',
            name='technology_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Technology_type'),
        ),
        migrations.AddField(
            model_name='employee_tech',
            name='technology',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Technology'),
        ),
        migrations.AddField(
            model_name='employee_tech',
            name='technology_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hr.Technology_type'),
        ),
    ]
