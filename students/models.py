from django.db import models



class Student(models.Model):
    students_id = models.CharField(max_length= 15)
    name = models.CharField(max_length= 30)
    branch = models.CharField(max_length= 20)

    def __str__(self):
        return self.name