
from django.shortcuts import render, get_object_or_404
from .models import Projec
# Create your views here.


def all_blogs(request):

    projects = Projec.objects.order_by('-title')[:5]
    return render(request, "blog/all_blogs.html", {'projects':projects})

def detail(request, blog_id):
    blog = get_object_or_404(Projec, pk=blog_id)
    return render(request, "blog/detail.html", {'blog': blog})

