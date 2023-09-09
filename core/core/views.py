from django.shortcuts import render,redirect
from django.http import HttpResponse
from RealEstate.models import Contact
from django.contrib import messages


# Create your views here.


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):

    try:
        if request.method == "POST":
            if request.POST.get("name") == "":
                return render(request, "contact.html", {"error": True})
            if request.POST.get("email") == "":
                return render(request, "contact.html", {"error": True})
            if request.POST.get("comment") == "":
                return render(request, "contact.html", {"error": True})
            name = request.POST.get('name')
            email = request.POST.get('email')
            comment = request.POST.get('comment')
            # print(f"Name: {name}, Email: {email}, Comment: {comment}")
            contact = Contact(name=name, email=email, comment=comment)
            contact.save()
            messages.success(request, 'Form submitted successfully!')
            
            

            
            
    except:
        message="Getting some Error Plz Try Again"        
    return render(request,'contact.html')