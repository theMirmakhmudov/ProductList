from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    ...


class Images(models.Model):
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.image.name


class Product(models.Model):
    image = models.ForeignKey('apps.Images', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()


class Home1(models.Model):
    image = models.ForeignKey('apps.Images', on_delete=models.CASCADE)
    txt = models.CharField(max_length=50)
    description = models.CharField(max_length=255)


class Home2(models.Model):
    recently_product = models.ForeignKey('apps.Product', on_delete=models.CASCADE)
