from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Category, Banner, Recommend, Article, Tag


def hello(request):
    return HttpResponse("hello world")


def index(request):
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]
    recommend = Article.objects.filter(recommend__id=1)[:3]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    print(allarticle)
    hot = Article.objects.all().order_by('views')[:10]
    remen = Article.objects.filter(recommend__id=2)[:6]
    tags = Tag.objects.all()
    print(allcategory)
    context = {
        'allcategory': allcategory,
        'banner': banner,
        'recommend': recommend,
        'allarticle': allarticle,
        'hot': hot,
        'remen': remen,
        'tags': tags,
    }
    # return HttpResponse(context['allarticle'])
    return HttpResponse(context['allcategory'])
    # return render(request, 'front/blog/index.html', context)
