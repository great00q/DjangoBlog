# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from System.models import *
# Register your models here.
class SystemAdmin(admin.ModelAdmin):
    list_display = ['id','name','describe','isActive','order']
    search_fields = ['id','name','isActive']
    list_per_page =5
    
class FriendAdmin(admin.ModelAdmin):
    list_display = ['id','siteName','url','isActive']
    list_filter = ['isActive']
    search_fields = ['id','siteName']
    list_per_page = 5
    
admin.site.register(Module,SystemAdmin)
admin.site.register(Friend,FriendAdmin)