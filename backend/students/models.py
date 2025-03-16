from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    rollnumber = models.IntegerField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.name} (Roll No: {self.rollnumber})"
