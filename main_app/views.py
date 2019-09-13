from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    return HttpResponse('Hello')

def signup(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      username = form.cleaned_data.get('username')
      messages.success(request, f'New Account Created: {username}')
      login(request, user)
      messages.info(request, f'You are now logged in as {username}')
      return redirect('landing')
    else:
      for msg in form.error_messages:
        messages.error(request, f'{msg}: {form.error_mesages[msg]}')
  
  form = NewUserForm()
  return render(request,'registration/signup.html', {'form':form})

def logout_request(request):
  logout(request)
  messages.info(request, 'Logged out successfuly!')
  return redirect('home')

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
        return redirect('landing')
      else:
        messages.error(request, 'Invalid username or password')
    else:
      messages.error(request, 'Invalid username or password')

  form = AuthenticationForm()
  return render(request, 'registration/login.html', {'form': form})
