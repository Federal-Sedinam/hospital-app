from django.db import models

class appointment(models.Model):
    name = models.CharField(max_length=25)
    service = models.CharField(max_length=100)
    discount = models.CharField(max_length=10) 
    def __str__(self):
        return self.service
