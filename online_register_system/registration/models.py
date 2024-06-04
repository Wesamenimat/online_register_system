from django.contrib.auth.models import User
from django.db import models

class College(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Major(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    prerequisite = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class StudentSubject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'subject')
