from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, UserForm, UserProfileForm
from .models import UserProfile, EmailVerifyRecord
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from utils.email_send import send_register_email

# there are logics of users application


class MyBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def active_user(request, active_code):
    """discarded"""
    all_records = EmailVerifyRecord.objects.filter(code=active_code)
    if all_records:
        for record in all_records:
            email = record.email
            user = User.objects.get(email=email)
            user.is_staff = True
            user.save()
    else:
        return HttpResponse('something wrong happen with the address')
    return redirect('users:login')


def login_view(request):
    """the logics related to log in"""
    # Determine which method the page is requesting
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # inner function to verify password and password
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # determine whether the user exists
                login(request, user)
                return redirect('blog:index')
            else:
                return HttpResponse('Failed :(')

    context = {'form': form}
    # pass the form to frontend
    return render(request, 'users/login.html', context)


def register(request):
    """the logics related to register"""
    if request.method != 'POST':
        form = RegisterForm()

    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.username = form.cleaned_data.get('email')
            new_user.save()
            # store the form
            # send_register_email(form.cleaned_data.get('email'), 'register')
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required(login_url='users:login')
def user_profile(request):
    """to do this action you need to log in"""
    user = User.objects.get(username=request.user)
    return render(request, 'users/user_profile.html', {'user': user})


def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required(login_url='users:login')
def editor_users(request):
    """logics related to edit profile of user"""
    # get current user
    user = User.objects.get(id=request.user.id)
    # Determine which method the page is requesting
    if request.method == 'POST':
        try:
            user_profile = user.userprofile
            form = UserForm(request.POST, instance=user)
            user_profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
            if form.is_valid() and user_profile_form.is_valid():
                form.save()
                user_profile_form.save()
                return redirect('users:user_profile')
        except UserProfile.DoesNotExist:
            # if the profile of a user doesn't exist, fill in default values.
            form = UserForm(request.POST, instance=user)
            user_profile_form = UserProfileForm(request.POST, request.FILES)
            # if the forms are all valid, save them.
            if form.is_valid() and user_profile_form.is_valid():
                form.save()
                new_user_profile = user_profile_form.save(commit=False)
                new_user_profile.owner = request.user
                new_user_profile.save()
                return redirect('users:user_profile')

    else:
        # just show the forms
        try:
            user_profile = user.userprofile
            form = UserForm(instance=user)
            user_profile_form = UserProfileForm(instance=user_profile)

        except UserProfile.DoesNotExist:
            form = UserForm(instance=user)
            user_profile_form = UserProfileForm()

    return render(request, 'users/editor_users.html', locals())
