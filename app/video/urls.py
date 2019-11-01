from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    # path('channels/', views.channels, name='channels'),
    # path('channel/<int:pk>/edit/', views.channel_edit, name='channel_edit'),
    # path('<slug:channel>/', views.video, name='video'),
    # path('<slug:channel>/<int:day>/<int:month>/<int:year>/<int:hour>/<int:minute>/', views.video, name='video'),

    path('channel/list/', views.ChannelList.as_view(), name='channel_list'),
    path('channel/create/', views.ChannelCreate.as_view(), name='channel_create'),
    path('channel/delete/<slug:slug>', views.ChannelDelete.as_view(), name='channel_delete'),
    path('channel/<slug:slug>/', views.ChannelUpdate.as_view(), name='channel_update'),
]
