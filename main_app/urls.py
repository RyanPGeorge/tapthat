from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('about/', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('home/cooler/', views.cooler, name='cooler'),
    path('home/my_restaurants/', views.my_restaurants, name='my_restaurants'),
    path('discover/', views.discover, name='discover'),
    path('beers/<int:beer_id>/', views.beer_detail, name='beer_detail'),
    path('cooler/<int:beer_id>/add/<int:user_id>', views.cooler_add, name='cooler_add'),
    path('restaurants/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('cooler/<int:restaurant_id>/add/<int:user_id>,', views.cooler_add_restaurant, name='cooler_add_restaurant'),
]