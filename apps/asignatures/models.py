from ast import mod
from django.db import models

# Create your models here.

class Semester(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Asignature(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.name


class AsignatureSemester(models.Model):
    group = models.CharField(max_length=10)
    asignature = models.ForeignKey(Asignature,on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return '{} {} {}'.format(self.asignature,self.group,self.semester)


class StudentAsignature(models.Model):
    asignature = models.ForeignKey(AsignatureSemester,on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

class Note(models.Model):
    name = models.CharField(max_length=200)
    asignature_semester = models.ForeignKey(AsignatureSemester,on_delete=models.CASCADE)
    percentage = models.DecimalField(max_digits=4,decimal_places=1)

class NoteUser(models.Model):
    note = models.DecimalField(max_digits=2,decimal_places=1)
    user = models.ForeignKey('accounts.User',on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)