from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfile(models.Model):
    USER_GENDER_TYPE = (
        ('male', 'male'),
        ('female', 'female'),
    )

    owner = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user')
    nike_name = models.CharField('nickname', max_length=50, blank=True, default='')
    bio = models.TextField('bio', max_length=200, blank=True, default='')
    feature = models.CharField('feature', max_length=100, blank=True, default='')
    birthday = models.DateField('birthday', null=True, blank=True)
    gender = models.CharField('gender', max_length=6, choices=USER_GENDER_TYPE, default='male')
    address = models.CharField('address', max_length=100, blank=True, default='')
    image = models.ImageField(upload_to='images/%Y/%m', default='images/default.png', max_length=100,
                              verbose_name='avatar')

    class Meta:
        verbose_name = 'UserProfile'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.owner.username


class EmailVerifyRecord(models.Model):

    SEND_TYPE_CHOICES = (
        ('register', 'register'),
        ('forget', 'forget password')
    )

    code = models.CharField('CAPTCHA', max_length=20)
    email = models.EmailField('EMAIL', max_length=35)
    send_type = models.CharField(choices=SEND_TYPE_CHOICES, default='register', max_length=20)

    class Meta:
        verbose_name = 'Captcha'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
