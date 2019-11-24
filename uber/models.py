from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    third_name = models.CharField(blank=True, null=True, max_length=50)
    inn = models.CharField(blank=True, null=True, max_length=50)

    def __str__(self):
        return self.username

class Company(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    master = models.CharField(max_length=100, blank=True, null=True) # Куратор
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    orgn = models.CharField(max_length=100, blank=True, null=True)
    inn = models.CharField(max_length=100, blank=True, null=True)
    kpp = models.CharField(max_length=100, blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    bik = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    linked_user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, null=True)

class University(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    master = models.CharField(max_length=100, blank=True, null=True) # Куратор
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    orgn = models.CharField(max_length=100, blank=True, null=True)
    inn = models.CharField(max_length=100, blank=True, null=True)
    kpp = models.CharField(max_length=100, blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    director = models.CharField(max_length=100, blank=True, null=True)
    bik = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)

    linked_user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, null=True)

class Project(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    discription = models.TextField()
    time = models.CharField(max_length=50, null=True)
    money = models.CharField(max_length=50, null=True)

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    university = models.ForeignKey(University, on_delete=models.PROTECT)

class Subscriber(models.Model):
    university = models.ForeignKey(University, on_delete=models.PROTECT)
    project = models.ForeignKey(Project, on_delete=models.PROTECT)

class Mentor(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)

    linked_user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, null=True)

class WorkGroup(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    mentor = models.ForeignKey(Mentor, on_delete=models.PROTECT)
    university = models.ForeignKey(University, on_delete=models.PROTECT)

class Student(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    phone = models.CharField(max_length=50, blank=False, null=True)
    email = models.CharField(max_length=50, blank=False, null=True)

    work_group = models.ForeignKey(WorkGroup, on_delete=models.PROTECT, null=True)
    university = models.ForeignKey(University, on_delete=models.PROTECT, null=True)

    linked_user = models.OneToOneField(CustomUser, on_delete=models.PROTECT, null=True)

