from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_completed = models.DateField()

    def __str__(self):
        return self.title

class Course(models.Model):
    name = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    completion_date = models.DateField()

    def __str__(self):
        return self.name

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issued_by = models.CharField(max_length=200)
    date_issued = models.DateField()

    def __str__(self):
        return self.name

