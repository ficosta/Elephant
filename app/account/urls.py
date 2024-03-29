from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('user/list/', views.UserList.as_view(), name='user_list'),
    #path('register/', views.register, name='register'),
    #path('edit/', views.edit, name='edit'),
    # path('users/', views.user_list, name='user_list'),
    #path('users/<username>/', views.user_detail, name='user_detail'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
