from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.lista_canais, name='lista_canais'),
    path('channels/', views.channels, name='channels'),
    path('<slug:channel>/', views.video, name='video'),
    path('<slug:channel>/<int:day>/<int:month>/<int:year>/<int:hour>/<int:minute>/', views.video, name='video'),
]
