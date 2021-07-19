from django.shortcuts import render,HttpResponse
from blogapp.models import Blog,Contact

#home page logic
def home(request):
    return render(request, 'index.html')

#blog page logic
def blog(request):
    blogs=Blog.objects.all()  #get info from model and render blogpage in bloghome.html
    context={'blogs':blogs}
    return render(request, 'bloghome.html',context)

#blogpost page logic
def blogpost(request,slug):
    blog=Blog.objects.filter(slug=slug).first() #get info from model and render blogpost page in blogpost.html
    context={'blog':blog}
    return render(request, 'blogpost.html',context)
    
#search page logic
def search(request):
    return render(request, 'search.html')

#contact page logic
def contact(request):
    if request.method =='POST':        #get info from user and save to db(we can saw the data in admin login)
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        instance=Contact(name=name,email=email,phone=phone,desc=desc)
        instance.save() #its save to db
    return render(request, 'contact.html')

