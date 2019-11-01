from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Channel, Clip
from datetime import datetime
from .forms import ChannelForm


class ChannelList(ListView):
    template_name = 'video/channel_list.html'
    model = Channel
    context_object_name = "channels"

class ChannelUpdate(UpdateView):
    template_name = "video/channel_form.html"
    model = Channel
    fields = '__all__'



class ChannelCreate(CreateView):
    model = Channel
    fields = '__all__'

class ChannelDelete(DeleteView):
    model = Channel

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
