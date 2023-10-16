from django.shortcuts import render, redirect
from .models import creators

# Create your views here.
def homepage(request):
    contents = creators.objects.all()
    return render(request,'homepage.html', {'contents':contents})
                  
                  
def add_creators(request):
    
    if request.method == "GET":
      return render(request, 'add_creators.html') 
    else:
        creators (
        firstname = request.POST.get("fname"),
        lastname  = request.POST.get("lname"),
        )  .save()
        return render(request, 'add_creators.html')
    
def digital_creators(request, id):
    content = creators.objects.get(id=id)
    if request.method == "GET":
        return render(request, 'update.html', {'content':content})   
    else:
        content.firstname = request.POST.get("fname")
        content.lastname = request.POST.get("lname")
        content.save()
        return redirect('homepage')
    
def delete_creators(request, id):
    content = creators.objects.get(id=id)
    content.delete()
    return redirect('homepage'  )    