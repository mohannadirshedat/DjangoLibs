from django.contrib import admin
from .models import Profile ,Company , ProfileAdmin



@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    fields = ['Name']
    search_fields = ['Name']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ['User_Name','Photo','Email','address','Phone','SSN','company']
    autocomplete_fields = ['company','User_Name']

admin.site.site_header = "SITECH SYSTEM"