from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    third_name = models.CharField(null=True, max_length=50)
    inn = models.CharField(null=True, max_length=50)

    def __str__(self):
        return self.username

class Company(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    amount_of_allowed_projects = models.IntegerField()

    linked_user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, null=True)

class University(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    master = models.CharField(max_length=100, blank=False, null=False) # Куратор

    linked_user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, null=True)

class Project(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    university = models.ForeignKey(University, on_delete=models.PROTECT)

class Subscriber(models.Model):
    university = models.ForeignKey(University, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)

class Mentor(models.Model):
    login = models.CharField(max_length=30, blank=False, null=True)
    password = models.CharField(max_length=30, blank=False, null=True)

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    third_name = models.CharField(max_length=50, null=True, blank=True)

    linked_user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, null=True)

class WorkGroup(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    mentor = models.ForeignKey(Mentor, on_delete=models.PROTECT)
    university = models.ForeignKey(University, on_delete=models.PROTECT)

class Student(models.Model):
    login = models.CharField(max_length=30, blank=False, null=True)
    password = models.CharField(max_length=30, blank=False, null=True)

    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    third_name = models.CharField(max_length=50, null=True, blank=True)

    work_group = models.ForeignKey(WorkGroup, on_delete=models.PROTECT)
    university = models.ForeignKey(University, on_delete=models.PROTECT, null=True)

    linked_user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, null=True)

