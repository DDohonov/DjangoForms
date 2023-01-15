from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        context['user_name'] = username
        context['password'] = password
        context['confirm_password'] = confirm_password
        if password != confirm_password:
            context['error_text'] = 'Паролі не співпадають'
        else:
            try:    
                User.objects.create_user(username=username, password=password)
                return redirect('succsesful')
            except IntegrityError:
                context["error_text"] = "Такий користувач вже існує"
    return render(request, 'app1/reg.html', context)
def reg_succsesful(request):
    return render(request, 'app1/succsesful_reg.html')

def welcome(request):
    if request.user.is_authenticated:
        return render(request, 'app1/welcome.html')
    else:
        return redirect('auth_page')

def auth_page(request):
    if request.method == 'POST':
        username = request.POST.get('user_name')
        password = request.POST.get('user_password')
        user = authenticate(request, username = username, password = password)
        if user != None:
            login(request, user)
            return redirect('welcome')
        
    return render(request, 'app1/auth.html')
def user_logout(request):
    logout(request)
    return redirect('auth_page')
