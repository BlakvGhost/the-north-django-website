from django.shortcuts import render

# Create your views here.
def home(request):
    index = ['','','','','','']
    context = {'index':index}
    return render(request,'home/home.html',context)