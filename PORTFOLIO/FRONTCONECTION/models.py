
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=1000,unique=True)
    description = models.TextField(null=True, blank=True)
    html_url = models.URLField(max_length=1000)
    readme = models.TextField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['title','html_url'])
        ]

class Contact(models.Model):
    name = models.CharField(max_length=1000,null=True, blank=True)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=1000)
    position = models.CharField(max_length=1000,null=True, blank=True)
    phone_number = PhoneNumberField()
    message = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['email'])
        ]

class corosel(models.Model):

    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=False)
    image = models.ImageField(upload_to='images/')
    html_url = models.URLField(max_length=1000)

    class Meta:
        indexes = [
            models.Index(fields=['title'])
        ]



class posts(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000,blank=True, null=True)
    description = models.TextField(null=True, blank=True, default='No description available')
    image = models.TextField(null=True, blank=True)
    html_url = models.TextField(max_length=1000,null=True, blank=True)
    date = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class services_des(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(null=True, blank=False)
    website = models.URLField(max_length=1000)
    image = models.ImageField(upload_to='seviceimg/')

    class Meta:
        indexes = [
            models.Index(fields=['title'])
        ]
