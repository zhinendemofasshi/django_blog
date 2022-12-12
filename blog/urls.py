from django.urls import path
from . import views
# this is the URL of the pages belonging to blog application
app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.category_list, name='category_list'),
    path('post/<int:post_id>', views.post_detail, name='post_detail'),
]
