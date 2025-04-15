# from django.contrib import admin
# from .models import UserBankAccount, UserAddress

# # Register your models here.
# admin.site.register(UserBankAccount) # register the model with admin site
# admin.site.register(UserAddress) # register the model with admin site 

from django.contrib import admin
from .models import UserBankAccount, UserAddress
# Register your models here.

admin.site.register(UserBankAccount)
admin.site.register(UserAddress)