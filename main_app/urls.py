from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('about/', views.about, name='about'),
    path('landing/', views.landing, name='landing'),
]