from django import forms
from .models import Channel


class ClipSearchForm(forms.Form):
    channel = forms.CharField(max_length=100)
    recordDate = forms.DateTimeField()


class ChannelSelectForm(forms.Form):
    channels = forms.ChoiceField(choices=[(channel.slug, channel.name) for channel in Channel.objects.filter(status=1)])
