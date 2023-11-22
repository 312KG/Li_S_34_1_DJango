from django.db import models

# Create your models here.

class Equipment(models.Model):
    image = models.ImageField(upload_to='images', null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.FloatField(default=0)
    rate = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



