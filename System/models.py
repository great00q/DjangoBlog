# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Module(models.Model):
    name = models.CharField(max_length=40)
    describe = models.CharField(max_length=255)
    isActive = models.BooleanField()
    order = models.SmallIntegerField(default=0)
    
    def __str__(self):
        return self.name.encode('utf-8')
    

        
class Friend(models.Model):
    siteName = models.CharField(max_length=60)
    url = models.CharField(max_length=100)
    isActive = models.BooleanField()
    
    def __str__(self):
        return self.siteName.encode('utf-8')

# class System(models.Model):
#     languageConf = models.CharField(max_length=20)
#     modulesConf = models.ForeignKey(Module)