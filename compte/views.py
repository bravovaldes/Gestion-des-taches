from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages


def inscription(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password")
        password2 = request.POST.get("confirm-password")
        print(username,password1,password2)
      
        if password1 != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
        else:
            
            if User.objects.filter(username=username).exists():
                messages.error(request, "Le nom d'utilisateur existe déjà.")
            else:

                user = User.objects.create_user(username=username, password=password1)
                messages.success(request, "Utilisateur créé avec succès.")
                return redirect('index')  

    return render(request, 'compte/inscription.html')


def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None :
            login(request,user)
            return redirect('dashboard')
        else:
              messages.error(request, "Le nom d'utilisateur ou le mot de passe est incorrecte")
    return render(request,'compte/login.html')


def deconnexion(request):
    logout(request)
    return redirect('index')