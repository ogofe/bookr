from django.contrib import admin
from django.contrib.auth.models import User
from .models import (
    Account,
    Cart,
    Wallet,
    Item,
    Product,
    Store,
    StoreLocation
)


for i in (Account, Cart,
          Wallet,  Item, Product,
          Store, StoreLocation
        ):
            admin.site.register(i)
