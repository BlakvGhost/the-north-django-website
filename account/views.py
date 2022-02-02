from django.shortcuts import render, redirect
from .forms import InscriptionForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def inscription(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = InscriptionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = InscriptionForm()
        context = {'form': form}
        return render(request, 'account/inscription.html', context)


def connexion(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            passwd = request.POST.get('mdp')
            user = authenticate(request, username=username, password=passwd)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password Incorrect")
        return render(request, 'account/connexion.html')


def logoutUser(request):
    logout(request)
    return redirect('connexion')
