from django.shortcuts import render,redirect
from django.http import HttpResponse
from event.forms import Category_add,Event_add,Create_participant
from django.contrib import messages
from event.models import Category,Event,Participant
from django.db.models import Q,Max,Min,Sum,Count
from datetime import date,time
from django.utils import timezone
from django.urls import reverse 
# ----------Default Database query ------------------------------


def home(request):
    BASE_CATA = Category.objects.all()
    BASE_EVENT = Event.objects.select_related('category').prefetch_related('participants').all()

    Type = request.GET.get('type','all')
    today = timezone.localdate()
    count = BASE_EVENT.aggregate(
        total = Count('id'),
        upcoming = Count('date',filter = Q(date__gt = today)),
        past_event = Count('date',filter = Q(date__lt = today))
    )
    users = Participant.objects.aggregate(count = Count('id'))

    print(today)
    

    if Type =='all':
        events = BASE_EVENT
    elif Type == 'Upcoming':
        events = BASE_EVENT.filter(date__gt=today)
    elif Type == 'past':
        events = BASE_EVENT.filter(date__lt=today)
    else:
        if Type.isdigit():
            category = BASE_CATA.get(id=int(Type))
            events = category.events.all()
        else:
            return redirect("home")
    
    context = {
                    'category':BASE_CATA,
                    'events':events,
                    'count':count,
                    'today':today,
                    'users':users
                }  
    return render(request,"Dashbord.html",context)  


    

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
        ev = Event.objects.get(id=id)
        evF = Event_add(instance = ev)

        context = {
            'event':evF
        }
        if request.method == "POST":
            evF = Event_add(request.POST,instance = ev)

            if evF.is_valid():
                evF.save()
                messages.success(request,"Event Add successfully!")
                return redirect("update",category,id)
        return render(request,"add_event.html",context)
    elif category == "participant":
        Parti_Cipant = Participant.objects.get(id=id)
        Participant_Form = Create_participant(instance = Parti_Cipant)


        if request.method == "POST":
            Participant_Form = Create_participant(request.POST,instance = Parti_Cipant)

            if Participant_Form.is_valid():
                Participant_Form.save()
                messages.success(request,"Successfully Update Participant!")
                return redirect("update",category,id)

        context = {
            'participant':Participant_Form
        }

        return render(request,"add_event.html",context)
        
def delete(request,category,id):
    if category == "events":
        if request.method == "POST":
            base = Event.objects.get(id=id)
            name = base.name
            base.delete()
            messages.success(request,f"Deleted Your Event: {name}!")
            return redirect(f"{reverse(home)}?type=all")