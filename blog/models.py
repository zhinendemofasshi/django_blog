from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models are like scheme of the database


class Category(models.Model):
    name = models.CharField(max_length=32, verbose_name="name")
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name="desc")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="add_date")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="mod_date")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name="name")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="add_date")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="mod_date")

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=61, verbose_name="title")
    desc = models.TextField(max_length=200, blank=True, default='', verbose_name="desc")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="category")
    content = models.TextField(verbose_name="content")
    tags = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.CASCADE, verbose_name="tag")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="owner")
    is_hot = models.BooleanField(default=False, verbose_name="is_hot")

    pv = models.IntegerField(default=0, verbose_name="pv")
    add_date = models.DateTimeField(auto_now_add=True, verbose_name="add_date")
    mod_date = models.DateTimeField(auto_now=True, verbose_name="mod_date")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
