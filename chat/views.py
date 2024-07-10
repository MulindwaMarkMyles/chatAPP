from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, MessageForm, CustomAuthenticationForm
from .models import User, Message
from django.http import JsonResponse

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_list_view(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'users.html', {'users': users})


@login_required
def send_message_view(request):
    form = MessageForm()
    return render(request, 'send_message.html', {'form': form})

@login_required
def send_message(request, id):
  
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receipient = User.objects.get(id=id)
            message.save()
            return JsonResponse("Done", safe=False)
    

@login_required
def inbox_view(request):
    messages = [message for message in Message.objects.all() if message.recipient == request.user or message.sender == request.user]
    return render(request, 'inbox.html', {'messages': messages})