from django.shortcuts import render,redirect
from m_app.models import category_db,product_database
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime
from webapp.models import contact_db


# Create your views here.
def index(req):
    data=datetime.datetime.now()
    cat=category_db.objects.all()
    no=cat.count()
    pro=product_database.objects.all()
    num=pro.count()
    return render(req,"index.html",{'data':data,'no':no,'num':num})
def add_cat(req):
    cat = category_db.objects.all()
    return render(req,"add_cat.html")
def view_cat(req):
    cat=category_db.objects.all()
    return render(req,"view_cat.html",{'cat':cat})
def save_cat(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.FILES['img']
        c=req.POST.get('desc')
        obj=category_db(c_name=a,c_img=b,c_desc=c)
        obj.save()
        return redirect(add_cat)
def edit_cat(req,c_id):
    cat=category_db.objects.get(id=c_id)
    return render(req,"edit.html",{'cat':cat})
def update_cat(req,c_id):
    if req.method=="POST":
        a=req.POST.get('name')
        c=req.POST.get('desc')
        try:
            b=req.FILES['img']
            fs=FileSystemStorage()
            file=fs.save(b.name,b)
        except MultiValueDictKeyError:
            file=category_db.objects.get(id=c_id).c_img
    category_db.objects.filter(id=c_id).update(c_name=a,c_img=file,c_desc=c)
    return redirect(view_cat)
def delete_cat(req,c_id):
    x=category_db.objects.filter(id=c_id)
    x.delete()
    return redirect(view_cat)
def add_pro(req):
    select=category_db.objects.all()
    return render(req,"add_pro.html",{'select':select})
def view_pro(req):
    pro=product_database.objects.all()
    return render(req,"view_pro.html",{'pro':pro})
def save_pro(req):
    if req.method=="POST":
        a=req.POST.get('select')
        b=req.POST.get('name')
        c=req.POST.get('mrp')
        d=req.POST.get('qua')
        e=req.FILES['img']
        f=req.FILES['img1']
        g=req.POST.get('desc')
        obj=product_database(cat_name=a,p_name=b,p_mrp=c,p_quan=d,p_img=e,p_img1=f,p_desc=g)
        obj.save()
        return redirect(add_pro)
def edit_pro(req,p_id):
    select=category_db.objects.all()
    pro=product_database.objects.get(id=p_id)
    return render(req,"edit_pro.html",{'pro':pro,'select':select})
def update_pro(req,p_id):
        if req.method == "POST":
            a = req.POST.get('select')
            b = req.POST.get('name')
            c = req.POST.get('mrp')
            d = req.POST.get('qua')
            g = req.POST.get('desc')
            try:
                e = req.FILES['img']
                fs=FileSystemStorage()
                file=fs.save(e.name,e)
            except MultiValueDictKeyError:
                file=product_database.objects.get(id=p_id).p_img
            try:
                f = req.FILES['img1']
                fs = FileSystemStorage()
                file1 = fs.save(f.name,f)
            except MultiValueDictKeyError:
                file1= product_database.objects.get(id=p_id).p_img1
        product_database.objects.filter(id=p_id).update(cat_name=a,p_name=b,p_mrp=c,p_quan=d,p_img=file,p_img1=file1,p_desc=g)
        return redirect(view_pro)
def delete_pro(req,p_id):
    x=product_database.objects.filter(id=p_id)
    x.delete()
    return redirect(view_pro)
def logins(req):
    return render(req,"login.html")
def login_page(request):
    if request.method=="POST":
        un=request.POST.get('user')
        pa=request.POST.get('pass')
        if User.objects.filter(username__contains=un).exists():
            user=authenticate(username=un,password=pa)
            if user is not None:
                login(request,user)
                request.session['username']=un
                request.session['password']=pa
                return redirect(index)
            else:
                return redirect(login_page)
        else:
            return redirect(login_page)
def delete_logout(req):
    del req.session['username']
    del req.session['password']
    return redirect(logins)
def contact_signup(req):
    con=contact_db.objects.all()
    return render(req,"contact_Signup.html",{'con':con})

def delete_con(req,c_id):
    x=contact_db.objects.filter(id=c_id)
    x.delete()
    return redirect(contact_signup)