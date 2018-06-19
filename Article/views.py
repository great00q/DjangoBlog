# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from Article.models import *
from System.models import *
# Create your views here.
def common():
    cate=Cate.objects.all().order_by('id')
    content=Article.objects.all().order_by('viewNum')
    models = Module.objects.filter(isActive='True').order_by('order')
    list=[cate,content,models]
    return list

def ModuleFun():
    
    dic = {}
    models = Module.objects.filter(isActive='True').order_by('order')
    for i in models:
        if i.name == '最新留言':
            comment = Comment.objects.all().order_by('postTime')
#             dic[i.name]=comment
            dic[i.order]=[i.name,comment]
        elif i.name == '热门文章':
            article = Article.objects.all().order_by('viewNum')
            dic[i.order]=[i.name,article]
        elif i.name == '最近发表':
            article = Article.objects.all().order_by('postTime')
            
            dic[i.order]=[i.name,article]
        elif i.name == '友情链接':
            friend = Friend.objects.filter(isActive='True')
            dic[i.order] = [i.name,friend]
        else:
            dic[i.order]=[i.name,'']
            
    return dic




def Index(request):
    cate = common()[0]
    content = common()[1]
    models = ModuleFun()
    return render(request,'body.html',{'cate':cate,'content':content,'models':models})

def Articles(request,id):
    cate = common()[0]
    models = ModuleFun()
    article = Article.objects.filter(id=id)
    comment = Comment.objects.filter(articleId=id)
    view = int(article[0].viewNum) + 1
    Article.objects.filter(id=id).update(viewNum=view)
    return render(request,'main.html',{'cate':cate,'content':article,'comment':comment,'models':models})


def Cates(request,id):
    cate = common()[0]
    models = ModuleFun()
    article = Article.objects.filter(cateId=id)
    return render(request,'body.html',{'cate':cate,'content':article,'models':models})
    

def Tags(request,id):
    
    pass

def Comments(request,id):
    if request.method == 'POST':
        try:
            userId = request.session['id']
        except KeyError:
            userId = '2'
        comment =request.POST.get('comment','')
        
        #Comment.objects.filter(articleId=id).update(content=comment)
        Comment.objects.create(author_id=userId,articleId_id=id,content=comment)
        commentNum = Comment.objects.filter(articleId=id).count()
        Article.objects.filter(id=id).update(commentNum=commentNum)
        
#     return Articles(request,id)
    return redirect('/blog/article/%s.html'%id)



          








































