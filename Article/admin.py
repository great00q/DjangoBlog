# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id','title','cateId','authorId','commentNum','viewNum']
    list_filter = ['cateId','tagId','authorId'] 
    search_fields = ['id','title','cateId','tagId','authorId']
    list_per_page =5
    
class CateAdmin(admin.ModelAdmin):
    list_display = ['id','parentId','cateName','count','order']
    list_filter = ['parentId']
    search_fields = ['id','parentId','cateName']
    list_per_page = 5
    
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','tagName','count','order']
    search_fields = ['id','tagName']
    list_per_page = 5
    
class CommentAdmin(admin.ModelAdmin):
    list_display =  ['id','articleId','parentId','content','postTime','idChecked']
    list_filter = ['articleId','author','idChecked']
    search_fields = ['id','articleId','parentId']
    list_per_page = 5
    
    
admin.site.register(Article,ArticleAdmin)
admin.site.register(Cate,CateAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Comment,CommentAdmin)