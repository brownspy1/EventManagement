from django.db import models

# Create your models here.
'''How may model Work'''
'''

Category--(1:M)-->Event--(M:M)-->Participant

'''


class Event(models.Model):
    name = models.CharField(max_length=250,null=False,blank=False)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE,default=1,related_name='events')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Participant(models.Model):
    name = models.CharField(max_length=250,null=False,blank=False)
    email = models.EmailField(unique=True)
    registered_events = models.ManyToManyField(Event,related_name='participants',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250,null=False,blank=False)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


