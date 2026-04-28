from django.shortcuts import render,redirect
from m_app.models import product_database,category_db
from webapp.models import contact_db,save_signup

# Create your views here.
def home_page(req):
    prod=category_db.objects.all()
    return render(req,"home.html",{'prod':prod})
def contact(req):
    return render(req,"contact.html")
def product(req):
    prod = category_db.objects.all()
    data=product_database.objects.all()
    return render(req,"product.html",{'data':data,'prod':prod})
def product_filtered(req,cate_name):
    category=product_database.objects.filter(cat_name=cate_name)
    return render(req,"product_filtered.html",{'category':category})
def single_products(req,p_id):
    single=product_database.objects.get(id=p_id)
    data = product_database.objects.all()
    return render(req,"single_product.html",{'single':single,'data':data})
def save_contacts(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('email')
        c=req.POST.get('msg')
        obj=contact_db(c_name=a,c_email=b,c_msg=c)
        obj.save()
        return redirect(contact)
def signin(req):
    return render(req,"signin.html")
def signup(req):
    return render(req,"signup.html")
def signup_save(req):
    if req.method=="POST":
        a=req.POST.get('name')
        b=req.POST.get('email')
        c=req.POST.get('pass')
        d=req.POST.get('repass')
        obj=save_signup(s_name=a,s_email=b,s_pass=c,s_repass=d)
        obj.save()
        return redirect(signup)

def about_us(req):
    return render(req,"about.html")
def signin_op(request):
    if request.method=="POST":
        un=request.POST.get('user')
        pa=request.POST.get('pass')
        if save_signup.objects.filter(s_name=un,s_pass=pa).exists:
            request.session['s_name']=un
            request.session['s_pass']=pa
            return redirect(home_page)
        else:
            return redirect(signin)
    else:
        return redirect(signin)
def logoutpage(request):
    del request.session['s_name']
    del request.session['s_pass']
    return redirect(home_page)


