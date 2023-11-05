from django.shortcuts import render, redirect
from blogsapp.models import Blog, Contact
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib import messages
import json
import requests
from django.conf import settings

# Create your views here. 
def home(request):
    blogs = Blog.objects.all().values()[0:2]

    return render(request, "index.html", {"myblog":blogs, "page_title":"Home Page"})

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("phone")
        message = request.POST.get("message")
        c = Contact(name = name, email = email, phone = number, message = message)
        c.save()  
        form_data = {
            'name':name,
            'email':email,
            'phone':number,
            'message':message,
        }
        message = '''
        Someone tried to connect you through the Blogs site.
        From: {}
        Message: {}
        Email: {}
        Phone: {}
        '''.format(form_data['name'], form_data['message'], form_data['email'],form_data['phone'])
        send_mail('You got a mail!', message, '', ['kirtirajput63969@gmail.com','saraju.work@gmail.com'])
        messages.success(request, "Your message has been sent ")
        return redirect("/contact")
    return render(request, "contact.html", {"page_title":"Contact Us"})




def blogs(request):
    blog = Blog.objects.all().values()[0:4]
    return render(request, "blogs.html", {"blogs":blog, "page_title":"Blogs "})

def services(request):
    return render(request, "services.html", {"page_title":"Our Services"})

def singleblog(request, blogid):
    blog = Blog.objects.get(id=blogid)
    return render(request, "single-blog.html", {"blog":blog})

def search(request):
    if request.method == "POST":
        query = request.POST.get("search")
        blogs = Blog.objects.filter(Q(title__contains = query)|Q(para1__contains = query))
    return render(request, "search.html", {"blogs" : blogs, "query" : query})

def news(request):
  
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=enter api key here"
    data = requests.get(url).json()
    articles = data['articles']
    myarticles = []
    for i in articles:
        if i["urlToImage"] is None:
            continue
        else:
            myarticles.append(i)
    return render(request,"news.html",{"articles":myarticles,"page_title":"Latest News"})


    

    
