from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, UserForm, UserProfileForm
from .models import UserProfile, EmailVerifyRecord
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from utils.email_send import send_register_email


class MyBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


def active_user(request, active_code):
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
    if request.method != 'POST':
        form = LoginForm()
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('users:user_profile')
            else:
                return HttpResponse('Failed :(')

    context = {'form': form}

    return render(request, 'users/login.html', context)


def register(request):
    if request.method != 'POST':
        form = RegisterForm()

    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.username = form.cleaned_data.get('email')
            new_user.save()

            send_register_email(form.cleaned_data.get('email'), 'register')
            return HttpResponse('Success!')

    context = {'form': form}
    return render(request, 'users/register.html', context)


@login_required(login_url='users:login')
def user_profile(request):
    user = User.objects.get(username=request.user)
    return render(request, 'users/user_profile.html', {'user': user})


def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required(login_url='users:login')
def editor_users(request):

    user = User.objects.get(id=request.user.id)
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
            form = UserForm(request.POST, instance=user)
            user_profile_form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid() and user_profile_form.is_valid():
                form.save()
                new_user_profile = user_profile_form.save(commit=False)
                new_user_profile.owner = request.user
                new_user_profile.save()
                return redirect('users:user_profile')

    else:
        try:
            user_profile = user.userprofile
            form = UserForm(instance=user)
            user_profile_form = UserProfileForm(instance=user_profile)

        except UserProfile.DoesNotExist:
            form = UserForm(instance=user)
            user_profile_form = UserProfileForm()

    return render(request, 'users/editor_users.html', locals())
