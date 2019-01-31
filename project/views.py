import threading
from django.shortcuts import render, redirect
from .models import Counter
from background_task import background
from datetime import datetime
import time
from django.contrib.auth.models import User
import os
from django.http import HttpResponse
# Create your views here.


def index(request):
    counter = Counter.objects.get(pk=1)
    return render(request, 'project/index.html', {'counter': counter})


def about(request):
    return render(request,'project/about.html')

def increment(request):
    if request.method == 'POST':
        counter = Counter.objects.get(pk=1)
        counter.count += 1
        counter.save()
        # print("POST", counter.count)
    # print("OUTSIDE")
    return redirect('index')

def increment_delay_view(request):
    if request.method == 'POST':
        print("POST Received", datetime.utcnow())
        t=threading.Thread(target=increment_delay)
        t.start()

    print("Redirected", datetime.utcnow())
    return redirect("index")



def increment_delay():
    print("sleeping")
    time.sleep(10)
    print('done sleeping')
    c = Counter.objects.get(pk=1)
    c.count+=1
    c.save()