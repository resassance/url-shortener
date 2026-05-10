from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('register/', views.register_view, name='register'),
    path('<str:short_code>/', views.redirect_view, name='redirect_url'),
]