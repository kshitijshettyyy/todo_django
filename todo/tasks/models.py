from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.title
class Student(models.Model):
    name=models.CharField(max_length=20)
    usn=models.IntegerField(primary_key=True)
    email=models.EmailField(max_length=30)
    branch=models.CharField(max_length=20)    
    def __str__(self):
        return self.name