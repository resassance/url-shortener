from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import RegisterForm
from .models import Link

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
    return render(request, 'links/index.html')

def redirect_view(request, short_code):
    link = get_object_or_404(Link, short_code=short_code)
    return redirect(link.original_url)