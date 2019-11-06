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
    context = {'channelSelectForm': ChannelSelectForm()}
    return render(request, 'channel_select.html', context)


# Ordenar por data https://www.vinta.com.br/blog/2017/advanced-django-querying-sorting-events-date/

def dashboard(request):
    return render(request, 'dashboard.html')


def ClipSelect(request):
    if request.method == 'POST':
        form = ChannelSelectForm(request.POST)
        print(form)
        if form.is_valid():
            channel = request.POST.get('channels')
            print(channel)
            clip = Clip.objects.filter(channel=channel).first()
            print(clip)
            context = {'channel': channel,
                       'clip': clip}
            return render(request, 'video_limpo.html', context=context)
    else:
        return redirect('video:channel_select')
