from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm,LoginForm
from django.urls import reverse_lazy
# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    success_url = reverse('home:home')
                    return  redirect(success_url)
                else:
                    return HttpResponse('Disabled account')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'login_form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            # Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})


def about(request):
    return render(request,
                  'about/about.html')


def contact(request):
    return render(request,
                  'contact/contact.html')


def test(request):
    return render(request,
                  'test/test.html')