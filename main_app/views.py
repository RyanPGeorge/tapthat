from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import SignUpForm
from .models import Beer, LikeBeerUser, Restaurant, LikeRestaurantUser

# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def about(request):
    return render(request, 'about.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def cooler(request):
  my_beers = LikeBeerUser.objects.filter(user=request.user)
  return render(request, 'cooler.html', { 'my_beers': my_beers})

@login_required
def my_restaurants(request):
  my_rests = LikeRestaurantUser.objects.filter(user=request.user)
  return render(request, 'my_restaurants.html', { 'my_rests': my_rests })

def cooler_add(request, beer_id, user_id):
  beer = Beer.objects.get(id=beer_id)
  user = User.objects.get(id=user_id)
  add = LikeBeerUser(beer=beer, user=user)
  add.save()
  messages.success(request, f'Successfully added {beer.name} to Cooler')
  return redirect('discover')

def cooler_add_restaurant(request, restaurant_id, user_id):
  rest = Restaurant.objects.get(id=restaurant_id)
  user = User.objects.get(id=user_id)
  add = LikeRestaurantUser(rest=rest, user=user)
  add.save()
  messages.success(request, f'Successfully added {rest.name} to Cooler')
  return redirect('discover')

def discover(request):
    beers = Beer.objects.all()
    restaurants = Restaurant.objects.all()
    my_beers = LikeBeerUser.objects.filter(user=request.user)
    return render(request, 'discover.html', {
       'beers': beers,
       'restaurants': restaurants,
       'my_beers': my_beers})

def beer_detail(request, beer_id):
    beer = Beer.objects.get(id=beer_id)
    rests = Restaurant.objects.filter(beers_on_tap=beer_id)
    untapped_rests = Restaurant.objects.exclude(beers_on_tap=beer_id)
    return render(request, 'beers/beer_detail.html',
    {
        'beer': beer,
        'rests': rests,
        'untapped_rests': untapped_rests,
    })

def restaurant_detail(request, restaurant_id):
  restaurant = Restaurant.objects.get(id=restaurant_id)
  print(restaurant)
  return render(request, 'restaurants/restaurant_detail.html',
  {
      'restaurant': restaurant,
  })


def signup(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'New Account Created: {username}')
      login(request, user)
      messages.info(request, f'You are now logged in as {username}')
      return redirect('home')
    else:
      for msg in form.error_messages:
        messages.error(request, f'{msg}: {form.error_messages[msg]}')
  
  form = SignUpForm()
  return render(request,'registration/signup.html', {'form':form})

def logout_request(request):
  logout(request)
  messages.info(request, 'Logged out successfuly!')
  return redirect('landing')

def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username=username, password=password)
      if user is not None:
        login(request, user)
        messages.info(request, f'Your are now logged in as {username}')
        return redirect('home')
      else:
        messages.error(request, 'Invalid username or password')
    else:
      messages.error(request, 'Invalid username or password')

  form = AuthenticationForm()
  return render(request, 'registration/login.html', {'form': form})
