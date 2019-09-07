from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Matr(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    fullname = models.CharField(max_length=128, blank=True)
    GENDER_CHOICES = (
            ('M', 'Male'),
            ('F', 'Female'),
    )
    gender = models.CharField(max_length=10,choices=GENDER_CHOICES, blank=True)
    age = models.PositiveIntegerField(null=True,blank=True)
    caste = models.CharField(max_length=36, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    comments = models.CharField(max_length=500, blank=True)
    location = models.CharField(max_length=40, blank=True)
    phone = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='media/photos/', null=True, blank=True)


    def __str__(self):
       return self.user.username
