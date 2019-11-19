from rest_framework import serializers

from video.models import Channel

from django import forms


class ChannelForm(forms.ModelForm):
    class Meta:
        model = Channel
        fields = "__all__"

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = "__all__"