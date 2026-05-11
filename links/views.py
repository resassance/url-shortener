from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from django.contrib.auth import login
from .forms import RegisterForm, LinkForm, LoginForm
from .models import Link
import uuid

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'links/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'links/login.html', {'form': form})

def index_view(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if not request.user.is_authenticated:
            return redirect('login')
        
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            return redirect('index')
    else:
        form = LinkForm()
    
    links = []
    if request.user.is_authenticated:
        links = Link.objects.filter(user=request.user).order_by('-created_at')
        
    return render(request, 'links/index.html', {'form': form, 'links': links})

def redirect_view(request, short_code):
    link = get_object_or_404(Link, short_code=short_code)
    Link.objects.filter(pk=link.pk).update(clicks_count=F('clicks_count') + 1)
    return redirect(link.original_url)