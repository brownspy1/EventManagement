from django.shortcuts import render,redirect
from django.http import HttpResponse
from event.forms import Category_add,Event_add,Create_participant
from django.contrib import messages
from event.models import Category,Event,Participant
# ----------Default Database query ------------------------------
BASE_QUERY = Category.objects.select_related('Category').prefetch_related('participants').all()

def home(request):
    return render(request,'Dashbord.html')

def add(request,id):
    if id == "category":
        category = Category_add()
        
        if request.method == 'POST':
            category = Category_add(request.POST)
            if category.is_valid():
                category.save()
                messages.success(request,"category Added successfully!")
                return redirect('add',id)
        
        return render(request,'add_event.html',{'category':category})

    elif id =="event":
        event = Event_add()
        if request.method == 'POST':
            event = Event_add(request.POST)
            if event.is_valid():
                event.save()
                messages.success(request,"Event Added successfully!")
                return redirect('add',id)
            
        return render(request,'add_event.html',{'event':event})
    elif id =="participant":
        participant = Create_participant()
        if request.method == 'POST':
            participant = Create_participant(request.POST)
            if participant.is_valid():
                participant.save()
                messages.success(request,"Participant is Created Successfully!")
                return redirect("add",id)
        return render(request,'add_event.html',{'participant':participant})   

def update(request,category,id):
    if category == "category":
        ct = Category.objects.get(id=id)
        ct_form = Category_add(instance = ct)

        context = {
            'category':ct_form
        }

        if request.method == "POST":
            ct_form = Category_add(request.POST, instance = ct)

            if ct_form.is_valid():
                ct_form.save()
                messages.success(request,'Category updated successfully!')
                return redirect("update",category,id)
        return render(request,'add_event.html',context)
    
    elif category =="event":
        pass