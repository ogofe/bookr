from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Account(models.Model):
    user            = models.OneToOneField(User, models.CASCADE, related_name='user')
    phone           = models.CharField(max_length=20)
    country         = models.CharField(max_length=50)
    state           = models.CharField(max_length=50)
    city            = models.CharField(max_length=50)
    photo           = models.ImageField(blank=True, upload_to='photo/')

    def __str__(self):
        return self.user.get_fullname()
    


class Cart(models.Model):
    user            = models.OneToOneField("Account", models.CASCADE)
    store           = models.OneToOneField("Store", models.CASCADE)
    items           = models.ManyToManyField("Item", blank=True, related_name='items')

    def __str__(self):
        return self.user.get_fullname()
    


class StoreLocation(models.Model):
    store:object    = None
    country         = models.CharField(max_length=50)
    state           = models.CharField(max_length=50)
    city            = models.CharField(max_length=50)
    zip             = models.CharField(max_length=50, blank=True)
    line            = models.CharField(max_length=50, blank=True)
    line2           = models.TextField(blank=True)

    def __str__(self):
        return f'{self.store.name}'

    

class Wallet(models.Model):
    owner:object    = None
    balance         = models.DecimalField(max_digits=10000, decimal_places=5)

    def __str__(self):
        return f'{self.owner.name}'
    

class Product(models.Model):
    name            = models.CharField(max_length=150)
    image           = models.ImageField(upload_to='products/')
    
    def __str__(self):
        return self.name
    


class Item(models.Model):
    product         = models.OneToOneField(Product, models.DO_NOTHING)
    price           = models.DecimalField(decimal_places=2, max_digits=10000)
    stock           = models.IntegerField(blank=True, null=True)
    store           = models.OneToOneField("Store", models.CASCADE)

    def __str__(self):
        return self.product.name
    


class Store(models.Model):
    owner           = models.OneToOneField(Account, models.CASCADE, related_name='owner')
    name            = models.CharField(max_length=120)
    photo           = models.ImageField(upload_to='stores/', blank=True)
    location        = models.OneToOneField(StoreLocation, models.CASCADE, related_name='location')
    hide            = models.BooleanField(default=True)
    wallet          = models.OneToOneField(Wallet, models.CASCADE, related_name='wallet')
    products        = models.ManyToManyField(Item, blank=True, related_name='products')

    def __str__(self):
        return self.name
