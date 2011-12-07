from myproject.python.models import Posts, Authors, Categories
from django.shortcuts import render_to_response, get_object_or_404
from django.http import Http404
from django.template import Context, loader
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
import os, time
from django.http import HttpResponse

DIRNAME = os.path.dirname(__file__)

def index(request):
    """
    index metodu tum katogorilerde bulunan en son gonderileri gosterir
    """
    try:
        all_posts = Posts.objects.all().filter().order_by('-post_pubdate')
        last_posts = Posts.objects.all().order_by('-post_pubdate')[:5]
        read_count = Posts.objects.all().order_by('-post_read_count')[:5]
        
        x = Context({
                  'all_posts':all_posts,
                  'last_posts':last_posts,
                  'read_count':read_count,
                  })
        
    except:
        raise Http404
            
    return render_to_response('python/index.html', x)

def category(request, category):
    """
    category metodu secilen katogoriye ait gonderileri gosterir
    orn :
            /python/blog
            /python/kitap
    """
    try:
        all_posts = Posts.objects.all().filter(post_category__category_name=category).order_by('-post_pubdate')
        last_posts = Posts.objects.all().order_by('-post_pubdate')[:5]
        read_count = Posts.objects.all().order_by('-post_read_count')[:5]
        
        x = Context({
                  'all_posts':all_posts,
                  'last_posts':last_posts,
                  'read_count':read_count,
                  })
        
    except:
        raise Http404
            
    return render_to_response('python/index.html', x)

@csrf_exempt
def show(request, category, link):
    """
    secilen gonderinin ayrintilari gosterilir
    """
    star1 = request.POST.get('star1', 0)
    star2 = request.POST.get('star2',0)    
    star3 = request.POST.get('star3',0)    
    star4 = request.POST.get('star4',0)    
    star5 = request.POST.get('star5',0)    
    try:
        all_posts_show = Posts.objects.get(post_category__category_name=category, post_link=link)
        last_posts = Posts.objects.all().order_by('-post_pubdate')[:5]
        #okunma sayisi
        all_posts_show.post_read_count = all_posts_show.post_read_count + 1
        all_posts_show.post_star = all_posts_show.post_star + int(star1) + int(star2) + int(star3) + int(star4) + int(star5)
        all_posts_show.save()
        #okunma sayisini goster
        read_count = Posts.objects.all().order_by('-post_read_count')[:5]        
        
        star_value = ['1', '2', '3', '4', '5']
        
        x = Context({
                  'all_posts_show':all_posts_show,
                  'last_posts':last_posts,
                  'read_count':read_count,
                  'star_value':star_value,
                  })
        
    except Posts.DoesNotExist:
        raise Http404
    return render_to_response('python/show.html', x)

@csrf_exempt
def show_star(request, category, link, value):
    """
    secilen gonderinin ayrintilari gosterilir
    """
    star1 = request.POST.get('star1', 0)
    star2 = request.POST.get('star2',0)    
    star3 = request.POST.get('star3',0)    
    star4 = request.POST.get('star4',0)    
    star5 = request.POST.get('star5',0)    
    try:
        all_posts_show = Posts.objects.get(post_category__category_name=category, post_link=link)
        last_posts = Posts.objects.all().order_by('-post_pubdate')[:5]
        #okunma sayisi
        all_posts_show.post_read_count = all_posts_show.post_read_count + 1
        all_posts_show.post_star = all_posts_show.post_star + int(star1) + int(star2) + int(star3) + int(star4) + int(star5)
        all_posts_show.save()
        #okunma sayisini goster
        read_count = Posts.objects.all().order_by('-post_read_count')[:5]        
        
        star_value = ['1', '2', '3', '4', '5']
        
        x = Context({
                  'all_posts_show':all_posts_show,
                  'last_posts':last_posts,
                  'read_count':read_count,
                  'star_value':star_value,
                  })
        
    except Posts.DoesNotExist:
        raise Http404
    return render_to_response('python/show2.html', x)

def codebank(request):
    """
    kod bankasi klasorundeki kodlari listeler
    """
    file_content = []
    file_read = ""
    
    try:
        file_list=os.listdir("/home/electrocoder/virtual-python/workspace/django-python/pythontr_org/myproject/static/python-kod-bankasi")
        #file_list = os.listdir("/home/electrocoder/webapps/pythontr_org/myproject/static/python-kod-bankasi")
        for i in file_list:            
            hfile=open("/home/electrocoder/virtual-python/workspace/django-python/pythontr_org/myproject/static/python-kod-bankasi/" + i)
            #hfile = open("/home/electrocoder/webapps/pythontr_org/myproject/static/python-kod-bankasi/" + i)
            file_read = hfile.read(55)
            file_content.append(file_read)
        
        x = Context({
                  'file_list':file_list,
                  'file_content':file_content,
                  'file_read':file_read,
                  })
        
    except Posts.DoesNotExist:
        raise Http404
    return render_to_response('codebank.html', x)
