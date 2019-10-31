from django.shortcuts import render, get_object_or_404

from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Channel, Clip
from datetime import datetime
from .forms import ChannelForm


def list_channels(request):
    channels = Channel.objects.all()

    return render(request, 'video/lista_canais.html', {'title': 'Lista de Canais', 'channels': channels})


def channels(request):
    channels = Channel.objects.all()

    new_channel = None

    if request.method == 'POST':
        # Um novo post será criado
        channel_form = ChannelForm(data=request.POST)
        if channel_form.is_valid():
            new_channel = channel_form.save()
    else:
        channel_form = ChannelForm()

    return render(request, 'video/channels.html', {'channels': channels,
                                                   'channel_form': channel_form,
                                                   'new_channel': new_channel})


def channel_edit(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    if request.method == "POST":
        channel_form = ChannelForm(request.POST, instance=channel)
        if channel_form.is_valid():
            channel = channel_form.save()
            return render('post_detail', pk=channel.pk)
    else:
        form = ChannelForm(instance=channel)
    return render(request, 'blog/channel_edit.html', {'channel_form': channel_form})


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
