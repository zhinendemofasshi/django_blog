from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=32, widget=forms.TextInput(attrs={
        'class': 'input is-primary',
        'placeholder': 'username/email',
    }))
    password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': 'password',
    }))

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username == password:
            raise forms.ValidationError("username should not be similar to password!")
        return password


class RegisterForm(forms.ModelForm):
    # username = forms.CharField(label='username', max_length=32, widget=forms.TextInput(attrs={
    #     'class': 'input is-primary',
    #     'placeholder': 'username/email',
    # }))
    email = forms.EmailField(label='email', max_length=32, widget=forms.EmailInput(attrs={
        'class': 'input',
        'placeholder': 'email',
    }))

    password = forms.CharField(label='password', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': 'password',
    }))

    password1 = forms.CharField(label='password again', min_length=6, widget=forms.PasswordInput(attrs={
        'class': 'input',
        'placeholder': 'password',
    }))

    class Meta:
        model = User
        fields = ('email', 'password')

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     exists = User.objects.filter(username=username).exists()
    #     if exists:
    #         raise forms.ValidationError('the username has already exists')
    #     return username
    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('the email has already exists')
        return email

    def clean_password1(self):
        if self.cleaned_data['password'] != self.cleaned_data['password1']:
            raise forms.ValidationError('the passwords are not the same')
        return self.cleaned_data['password1']


class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'input',
    }))

    class Meta:
        model = User
        fields = ('email',)


class UserProfileForm(forms.ModelForm):
    nike_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input'
    }))

    bio = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'textarea'
    }))
    feature = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input'
    }))
    birthday = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'input'
    }))

    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'input'
    }))

    gender = forms.CharField(widget=forms.Select(attrs={
        'class': 'select'

    },
        choices=(
            ('male', 'male'),
            ('female', 'female'),
        )))

    class Meta:
        model = UserProfile
        fields = ('nike_name', 'bio', 'feature', 'birthday', 'gender', 'address', 'image')
