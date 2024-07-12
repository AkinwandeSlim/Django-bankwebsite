from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def home(request):
    return render(request, 'home.html',{'title':'Homepage'})



def about(request):
    return render(request, 'about.html',{'title':'About US'})



def blog(request):
    return render(request, 'blog.html',{'title':'Blog'})



def contact(request):
    return render(request, 'contact.html',{'title':'Contact'})


def faq(request):
    return render(request, 'faQ.html',{'title':'FAQs'})
