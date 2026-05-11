from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import RegisterForm, LinkForm
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

def index_view(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if not request.user.is_authenticated:
            return redirect('login')
        
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            
            link.short_code = str(uuid.uuid4())[:6]
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
    link.clicks_count += 1
    link.save()
    return redirect(link.original_url)