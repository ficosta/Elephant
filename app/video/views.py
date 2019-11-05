from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Channel, Clip
from datetime import datetime


class ChannelList(ListView):
    template_name = 'channel_list.html'
    model = Channel
    context_object_name = 'channels'


class ChannelUpdate(UpdateView):
    template_name = 'channel_form.html'
    model = Channel
    fields = ['name', 'hiresLifetime', 'lowresLifetime', 'logo', 'status']
    success_url = '/video/channel/list/'


class ChannelCreate(CreateView):
    model = Channel
    template_name = 'channel_form.html'
    fields = ['name', 'hiresLifetime', 'lowresLifetime', 'logo', 'status']
    success_url = '/video/channel/list/'


class ChannelDelete(DeleteView):
    model = Channel
    success_url = '/video/channel/list/'


def ClipDetail(request, date, hour, channel_id):
    model = Clip


#Ordenar por data https://www.vinta.com.br/blog/2017/advanced-django-querying-sorting-events-date/

def dashboard(request):
    return render(request, 'dashboard.html')


def video(request, channel=None, date=None, time=None):
    if channel is None:
        HttpResponseRedirect(reverse('video:lista_canais'))
    else:
        if request.method == 'POST':
            # Efetua a busca com data e Hora
            date = request.POST.get('date')
            time = request.POST.get('time')

            diaHora = datetime.strptime(('{} {}'.format(date, time)), "%Y-%m-%d %H:%M").strftime("%Y-%m-%d %H:%M:%S")
            print(diaHora)
            clip = Clip.objects.filter(channel__slug=channel, recordDate__lte=diaHora).order_by('-recordDate').first()
        else:
            clip = Clip.objects.filter(channel__slug=channel).order_by('-recordDate').first()

    return render(request, 'video/video.html', {'title': 'Player', 'clip': clip, 'date': date, 'time': time})
