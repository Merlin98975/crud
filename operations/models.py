from django.db import models


class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    dept = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=100)

    def __str__(self):
        return self.emp_name


