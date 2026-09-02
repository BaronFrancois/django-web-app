from django.shortcuts import render

# ~/projects/django-web-app/merchex/listings/views.py

from django.http import HttpResponse
from django.shortcuts import render
from .models import Band

def hello(request):
    bands = Band.objects.all()
    items=''.join(
        f"<li>{band.name}</li>"
        for band in bands
    )
    return render(request,'listings/hello.html',
        {'bands': bands})
