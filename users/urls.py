from django.urls import path
from . import views
# this is the URL of the pages belonging to users application
app_name = 'users'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('active/<active_code>', views.active_user, name='active_user'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('editor_users/', views.editor_users, name='editor_users'),
]
