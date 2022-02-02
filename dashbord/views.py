from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core.exceptions import ValidationError
import os.path
from .forms import Blog,Musique,Files
from .models import fichiers as Fich,Pmusik
# Create your views here.


def index(request):
    return render(request, 'dashbord/admin.html')

def blog(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    else:
        if request.method == 'POST':
            blogform = Blog(request.POST,request.FILES)
            if blogform.is_valid():
                inwait = blogform.save(commit=False)
                inwait.post_author = request.user
                inwait.post_ua = request.META['HTTP_USER_AGENT']
                inwait.post_content = request.POST.get('post_content')
                inwait.save()
        else:
            blogform = Blog
        context={'form':blogform,}
        return render(request, 'dashbord/publishblog.html',context)

def musique(request):
    if not request.user.is_authenticated:
        return redirect('connexion')
    else:
        if request.method == 'POST':
            fields = Musique(request.POST,request.FILES)
            if fields.is_valid():
                notYet = fields.save(commit=False)
                notYet.post_author = request.user
                notYet.post_ua = request.META['HTTP_USER_AGENT']
                notYet.save()
        else:
            fields = Musique
        context = {'forms':fields,}
        return render(request,'dashbord/publishmsq.html',context)

def upload(request):
    if request.method == "POST":
        fichier = Files(request.POST,request.FILES)
        if fichier.is_valid():
            new_file = fichier.save(commit=False)
            new_file.file_size = 111
            new_file.file_type = request.POST.get('file_type')
            new_file.file_kind = 'musique'
            new_file.file_post_author = request.user
            new_file.file_post_id = ''
            new_file.file_duration = 3
            new_file.file_original_name = 'levy'
            new_file.file_post_ua = request.META['HTTP_USER_AGENT']
            new_file.save()

    else:
        fichier = Files
    context = {'files':fichier}
    return render(request,'dashbord/demo.html',context)

def demo(request):
    demox = request.data
    context = {'demo':demox}
    return render(request,'base/demo.html',context)