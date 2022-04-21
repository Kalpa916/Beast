from django.db import models

# Create your models here.
class StudebtRegistration(models.Model):
    studentName=models.CharField(max_length=100)
    studentId=models.IntegerField()
    studentClass=models.IntegerField()
    StudentGuardiandName=models.CharField(max_length=100)
    StudentCollegeName=models.CharField(max_length=100)
    studentPasssword=models.CharField(max_length=100)
