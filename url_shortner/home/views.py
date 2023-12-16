from . import shortner
from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def home_(r):
    return render(r,"home.html")
def Contect(r):
    return render(r,"contect.html")
def about(r):
    return render(r,"about.html")
def short(r):
    result=""
    if r.method=="POST":
        result=shortner.short(r.POST["url"])
    return render(r,"shortner.html",{"result":result})