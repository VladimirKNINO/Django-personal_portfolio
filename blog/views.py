
from django.shortcuts import render
from .models import Projec
# Create your views here.


def all_blogs(request):
    projects = Projec.objects.all()
    return render(request, "blog/all_blogs.html", {'projects':projects})
