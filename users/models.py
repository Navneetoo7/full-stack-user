from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_image = models.ImageField(upload_to='image/')
    email = models.EmailField(max_length=100)
    institution = models.CharField(max_length=100)
    loft = models.CharField(max_length=100)
    country = models.CharField(max_length=10)
    password = models.CharField(max_length=100)



    def __str__(self):
        return self.first_name + " " +self.last_name