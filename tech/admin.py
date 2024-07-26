from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header ='CYBRIA TECH ADMIN'
admin.site.site_title ='CYBRIA TECH PORTAL'
admin.site.index_title='WELCOME TO CYBRIA TECH ADMIN PORTAL'
   
     

    
    
class ContactAdminSite(admin.ModelAdmin):
    model = Contacts    

    list_display =('name', 'email', 'subject')

    list_filter = ['email', 'subject']

    search_fields = ['name', 'email', 'subject']

    fieldsets =[
        ("Contacts Details",{"fields":['name', 'email', 'subject', "message"]}),    
               ]


class DeveloperAdminSite(admin.ModelAdmin):
    model = Becomeadeveloper    

    list_display =('firstname', 'lastname','phone', 'email', "skills")

    list_filter = ['firstname', 'lastname', 'email', "skills"]

    search_fields = ['firstname', 'lastname', 'email', "skills"]

    fieldsets =[
        ("Developer's Details",{"fields":['firstname','lastname', 'phone', 'email', "skills"]}),    
               ]
    
 
            
    


admin.site.register(Becomeadeveloper, DeveloperAdminSite)
admin.site.register(Contacts, ContactAdminSite)
