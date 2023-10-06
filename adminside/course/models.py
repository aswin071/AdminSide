from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=200, unique=True)
    subtitle = models.TextField(max_length=500, blank=True)
    description = models.TextField(max_length=500, blank=True)
    active=models.BooleanField(default=True)
    image = models.ImageField(upload_to ='photos/product',blank=False)

    def __str__(self):
        return self.title