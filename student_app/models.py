from django.db import models

# Create your models here.
import uuid
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField(unique=True,null=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.FloatField()

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.marks}"
