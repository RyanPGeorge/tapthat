from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('cooler/', views.cooler, name='cooler'),
    path('discover/', views.discover, name='discover'),
]