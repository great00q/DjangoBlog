# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#定义分类表
class Cate(models.Model):
    parentId = models.SmallIntegerField(default=0)
    cateName = models.CharField(max_length=20)
    count = models.SmallIntegerField(default=0)
    order = models.SmallIntegerField(default=0)
    
    def __str__(self):
        return self.cateName.encode('utf-8')

#定义标签表    
class Tag(models.Model):
    tagName = models.CharField(max_length=20)
    count = models.SmallIntegerField(default=0)
    order = models.SmallIntegerField(default=0)
    
    def __str__(self):
        return self.tagName.encode('utf-8')
  
#创建文章表
class Article(models.Model):
    title = models.CharField(max_length=255)
    status = models.SmallIntegerField(default=0)
    cateId = models.ForeignKey(Cate)
    tagId = models.ManyToManyField(Tag)
    authorId = models.ForeignKey(User)
    describe = models.TextField(default='None')
    content = models.TextField()
    isTop = models.BooleanField()
    isLock = models.BooleanField()
    postTime = models.DateField(auto_now_add=True)
    commentNum = models.CharField(max_length=8,default=0)
    viewNum = models.CharField(max_length=8,default=0)
    
    def __str__(self):
        return self.title.encode('utf-8')

#定义评论表    
class Comment(models.Model):
    author = models.ForeignKey(User,default=None)
    articleId = models.ForeignKey(Article)
    parentId =  models.SmallIntegerField(default=0)
    content = models.TextField()
    postTime = models.DateField(auto_now_add=True)
    idChecked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.content.encode('utf-8')
#class upload(models.Model):
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    