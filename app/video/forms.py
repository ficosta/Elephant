from django import forms


class ClipSearchForm(forms.Form):
    channel = forms.CharField(max_length=100)
    recordDate = forms.DateTimeField()
