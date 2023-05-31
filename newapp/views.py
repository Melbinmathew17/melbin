from django.shortcuts import render,redirect
from newapp.models import positiondb,playerdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User

# Create your views here.
def indexpage(request):
    return render(request,"indexpage.html")

def positionpage(request):
    return render(request,"position.html")

def saveposition(request):
    if request.method=="POST":
        p=request.POST.get('position')
        a=request.POST.get('country')
        im=request.FILES['image']
        obj=positiondb(position=p,country=a,image=im)
        obj.save()
        return redirect(positionpage)

def displaypage(request):
    data=positiondb.objects.all()
    return render(request,"display.html",{'data':data})

def editposition(request,dataid):
    data=positiondb.objects.get(id=dataid)
    return render(request,"editposition.html",{'data':data})

def updateposition(request,dataid):
    if request.method=="POST":
        p = request.POST.get('position')
        a = request.POST.get('country')
        try:
            im=request.FILES['image']
            fs= FileSystemStorage()
            file= fs.save(im.name,im)
        except MultiValueDictKeyError:
            file=positiondb.objects.get(id=dataid).image
        positiondb.objects.filter(id=dataid).update(position=p,country=a,image=file)
        return redirect(displaypage)

def deleteposition(request,dataid):
    data=positiondb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaypage)

def playerpage(request):
    data=positiondb.objects.all()
    return render(request,"addplayer.html",{'data':data})

def saveplayer(request):
    if request.method=="POST":
        c=request.POST.get('playerposition')
        p=request.POST.get('playername')
        d=request.POST.get('age')
        q=request.POST.get('club')
        im=request.FILES['image']
        obj=playerdb(playerposition=c,playername=p,age=d,club=q,image=im)
        obj.save()
        return redirect(playerpage)

def displayplayer(request):
    data = playerdb.objects.all()
    return render(request, "displayplayer.html",{'data': data})

def editplayer(request,dataid):
    data=playerdb.objects.all()
    products=playerdb.objects.get(id=dataid)
    return render(request,"editplayer.html",{'data':data, 'products':products})

def updateplayer(request,dataid):
    if request.method=="POST":
        c = request.POST.get('playerposition')
        p = request.POST.get('playername')
        d = request.POST.get('age')
        q = request.POST.get('club')

        try:
            im=request.FILES['image']
            fs= FileSystemStorage()
            file= fs.save(im.name,im)
        except MultiValueDictKeyError:
            file = playerdb.objects.get(id=dataid).image
        playerdb.objects.filter(id=dataid).update(playerposition=c,playername=p,age=d,club=q,image=file)
        return redirect(displayplayer)


def deleteplayer(request, dataid):
    data =playerdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayplayer)

def adminpage(request):
    return render(request,"adminlogin.html")

def adminlogin(request):
    if request.method=="POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r,password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(indexpage)
            else:
                return redirect(adminlogin)

    else:
        return redirect(adminlogin)

def adminlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(adminlogin)
