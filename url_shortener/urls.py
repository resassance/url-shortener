from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from links import views as links_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='links/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', links_views.register_view, name='register'),
    path('', include('links.urls')),
]