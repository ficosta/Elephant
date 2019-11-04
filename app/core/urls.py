from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('log/list/', views.LogList.as_view(), name='log_list'),
    path('log/create/', views.LogCreate.as_view(), name='log_create'),
    path('log/delete/<int:pk>', views.LogDelete.as_view(), name='log_delete'),
    path('log/update/<int:pk>/', views.LogUpdate.as_view(), name='log_update'),

    path('notification/list/', views.NotificationList.as_view(), name='notification_list'),
    path('notification/create/', views.NotificationCreate.as_view(), name='notification_create'),
    path('notification/delete/<int:pk>', views.NotificationDelete.as_view(), name='notification_delete'),
    path('notification/update/<int:pk>/', views.NotificationUpdate.as_view(), name='notification_update'),
]
