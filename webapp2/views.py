from django.shortcuts import render
from newapp.models import positiondb,playerdb

# Create your views here.
def homepage(request):
    data=positiondb.objects.all()
    return render(request,"home.html",{'data':data})

def playerspage(request,catg):
    products=playerdb.objects.filter(playerposition=catg)
    return render(request,"players.html",{'products':products})

def singleplayer(request,dataid):
    data=playerdb.objects.get(id=dataid)
    return render(request,"singleplayer.html",{'data':data})