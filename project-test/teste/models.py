from django.db import models

class Teste(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    work_at = models.CharField(max_length=50, null=False)
    salary = models.FloatField(max_length=7)
