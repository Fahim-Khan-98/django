from django.db import models

# Create your models here.


class contact(models.Model):
    name = models.CharField(max_length=100,blank=False)
    email = models.TextField(max_length=100,blank=False)
    subject = models.TextField(max_length=700,blank=False)
    message = models.TextField(max_length=1000,blank=False)



    def __str__(self):
        return self.subject