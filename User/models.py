# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInfo(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    status = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    createTime = models.DateField(auto_now_add=True)
    

    