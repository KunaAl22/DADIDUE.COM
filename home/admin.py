from django.contrib import admin
from home.models import Contact


# Register your models here.
from .models import *
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)

