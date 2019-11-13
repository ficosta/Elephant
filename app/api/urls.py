from django.urls import path, include
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.TestView.as_view(), name='test'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
