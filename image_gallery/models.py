from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Catagory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name


class Image(models.Model) :
    owner       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField()
    catagory    = models.ForeignKey(Catagory, on_delete=models.DO_NOTHING)
    created_at  = models.DateTimeField(auto_now_add=True)
    photo       = models.ImageField(upload_to="image_gallery")
    price       = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.description
    
    def owner_name(self):
        return self.owner.first_name + ' ' + self.owner.last_name
    
    def description_text(self):
        return self.description[:50] + ' ....'

