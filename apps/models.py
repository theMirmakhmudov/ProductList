from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    ...


class Images(models.Model):
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name_plural = "Images"


class Product(models.Model):
    image = models.ForeignKey('apps.Images', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = "Product"


class Home1(models.Model):
    image = models.ForeignKey('apps.Images', on_delete=models.CASCADE)
    txt = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.txt

    class Meta:
        verbose_name_plural = "Home1"


class Home2(models.Model):
    recently_product = models.ForeignKey('apps.Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.recently_product.product_name

    class Meta:
        verbose_name_plural = "Home2"


class Persons(models.Model):
    image = models.ImageField(upload_to="Person", null=True, blank=True)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name_plural = "Persons"


class About1(models.Model):
    image = models.ForeignKey('apps.Images', on_delete=models.CASCADE)
    txt = models.CharField(max_length=55)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.txt

    class Meta:
        verbose_name_plural = "About"


class AboutPerson(models.Model):
    image = models.ForeignKey('apps.Persons', on_delete=models.CASCADE)
    person_name = models.CharField(max_length=55)
    staff = models.CharField(max_length=25)

    def __str__(self):
        return self.person_name

    class Meta:
        verbose_name_plural = "AboutPerson"


class Contact(models.Model):
    image = models.ForeignKey('apps.Images', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name_plural = "Contact"


class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "ContactForm"
