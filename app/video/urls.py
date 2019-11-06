from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.dashboard, name='video_dashboard'),
    path('channel/select/', views.channelSelect, name='channel_select'),
    path('channel/list/', views.ChannelList.as_view(), name='channel_list'),
    path('channel/create/', views.ChannelCreate.as_view(), name='channel_create'),
    path('channel/delete/<slug:slug>', views.ChannelDelete.as_view(), name='channel_delete'),
    path('channel/update/<slug:slug>/', views.ChannelUpdate.as_view(), name='channel_update'),
    path('clip/', views.ClipSelect, name='clip'),
]
