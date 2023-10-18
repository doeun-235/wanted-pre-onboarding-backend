from django.db import models

# Create your models here.
class Item(models.Model):
    company_id = models.IntegerField(editable=False)
    position = models.CharField(max_length=100)
    award = models.IntegerField()
    content = models.CharField(max_length=10000)
    skills = models.CharField(max_length=100)