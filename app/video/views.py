from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from .models import Channel, Clip
from datetime import datetime
from .forms import ChannelSelectForm


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


# # def ClipDetail(request, date, hour, channel_id):
#     model = Clip

def channelSelect(request):
    if request.method == 'POST':
        form = ChannelSelectForm(request.POST)
        if form.is_valid():
            channel = request.POST.get('channels')
            return redirect('video:channel', channel)
    else:
        context = {'channelSelectForm': ChannelSelectForm()}
        return render(request, 'channel_select.html', context)


# Ordenar por data https://www.vinta.com.br/blog/2017/advanced-django-querying-sorting-events-date/

def channel(request, slug=None):
    if not slug:
        return redirect('video:channel_select')
    else:
        if request.method == 'POST':
            #Busca pelo clip data/hora
            pass
        else:
            #Busca ultimo video
            context = {'slug': slug}
            return render(request, 'video_limpo.html', context=context)