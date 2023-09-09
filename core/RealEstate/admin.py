from django.contrib import admin
from RealEstate.models import Contact

# Register your models here.

class AdminUser(admin.ModelAdmin):
    list_display =('name', 'email','comment')
    
admin.site.register(Contact,AdminUser)    