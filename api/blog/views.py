from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Category, Banner, Recommend, Article, Tag
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth.models import User


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


@csrf_exempt
def login(request):
    if request.method == "POST":
        from django.contrib.auth.hashers import make_password, check_password
        json_result = json.loads(request.body)
        print(json_result)
        username = json_result.get("username")
        passwd = json_result.get("password")
        print(username)
        user = User.objects.filter(username=username).first()
        print(user)
        if user:
            if check_password(passwd, user.password):
                request.session['is_login'] = '1'
                request.session['username'] = username
                request.session['user_id'] = user.id
            adminUser = {
                "id": user.id,
                "username": username
            }
            return HttpResponse(json.dumps(adminUser))
        return HttpResponse(json.dumps({"code": 2222}))
