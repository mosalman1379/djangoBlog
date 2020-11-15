from django.shortcuts import render,HttpResponse
from . import models

def article_list(request):
        articles=models.Article.objects.all().order_by('date')
        return render(request,'articles/articlelist.html',{'articles':articles})
def article_detail(request,slug):
        return HttpResponse(slug)
