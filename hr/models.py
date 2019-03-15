from django.contrib import admin
from django.db import models


class Technology(models.Model):
    Langs = (
        ('PHP', 'PHP'),
        ('Python', 'Python'),
        ('JavaScript', 'JavaScript'),
        ('C#', 'C#'),
        ('Java', 'Java'),
        ('C', 'C'),
        ('HTML', 'HTML'),
        ('CSS', 'CSS'),
        ('SQL', 'SQL'),
        ('TypeScript', 'TypeScript'),
        ('Ruby', 'Ruby'),
    )
    name = models.CharField(choices=Langs, max_length=100, unique=True)
    description = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='media/images/technology/', blank=True, null=True)

    def __str__(self):
        return "{} ".format(self.name)


class Technology_type(models.Model):
    name = models.CharField(max_length=50, unique=True)
    technology = models.ForeignKey(Technology,on_delete=models.CASCADE)

    def __str__(self):
        return "{} ".format(

            self.name
        )

    class Meta:
        ordering = ('name',)


class Other(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return "{} ".format(

            self.name
        )


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50, null=True, blank=True)
    work_experience = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(max_length=20, null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='media/images/emp/', blank=True, null=True)

    def __str__(self):
        return "{} {}".format(
            self.first_name,
            self.last_name)


class Employee_tech(models.Model):
    Skills = (
        ('Junior', 'Junior'),
        ('Mid', 'Mid'),
        ('Senior', 'Senior')
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, unique=True)
    technology = models.ManyToManyField(Technology)
    technology_type = models.ManyToManyField(Technology_type)
    other = models.ManyToManyField(Other)
    skil_level = models.CharField(max_length=30, choices=Skills)
