from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from datetime import datetime
from .models import BlogPost,Contacts
from django.db.models import Q
from django.core.paginator import Paginator
# Create your views here.


def pagination(request):
    item_per_page = 5
    post_list = BlogPost.objects.all()
    paginator = Paginator(post_list, item_per_page)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    final_product = paginator.get_page(page_number)
    total_page = final_product.paginator.num_pages
    page_obj=[n+1 for n in range(total_page)]
    data={"page": page_obj,'posts':final_product}
    return data

def post(request):
    return render(request, "posts.html", pagination(request))

def index(request):
    # return HttpResponse('Hello, world. You\'re at the polls index.')
    return render(request, 'index.html',pagination(request))

def search(request, METHOD=['GET','POST']):
    item_per_page = 5
    if request.method == 'GET':
        item = request.GET.get('keywords')
        posts = BlogPost.objects.filter(Q(title__icontains=item) | Q(subtitle__icontains=item)| Q(description__icontains=item))
    

    
    # post_list = BlogPost.objects.all()
    paginator = Paginator(posts, item_per_page)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    final_product = paginator.get_page(page_number)
    total_page = final_product.paginator.num_pages
    page_obj=[n+1 for n in range(total_page)]
    data={"page": page_obj,'posts':final_product, 'keyword':item}
    # data={
    #     'posts':posts
    # }
    return render(request,'search.html',data)
# def post(request):
#     posts = BlogPost.objects.all()
    
#     data={
#         'posts':posts
#     }
#     return render(request, 'posts.html',data)

def about(request):
    return render(request, 'about.html')


def desc(request,id):
    posts = BlogPost.objects.filter(id=id)
    data={
        'posts':posts
    }
    return render(request, 'post.html',data)

def contact(request,Method=['GET','POST']):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        cont = Contacts(name = name, email = email, phone = phone, msg=msg, date = datetime.today())
        cont.save()
        
        return redirect('/contactUs',{'msg':"Your message has been sent successfully.... We will contact you latter..."})

#     pass

    return render(request, 'contact.html')
 
