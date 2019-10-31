from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.list_channels, name='list_channels'),
    path('channels/', views.channels, name='channels'),
    path('channel/<int:pk>/edit/', views.channels, name='channel_edit'),
    # path('<slug:channel>/', views.video, name='video'),
    # path('<slug:channel>/<int:day>/<int:month>/<int:year>/<int:hour>/<int:minute>/', views.video, name='video'),
]
