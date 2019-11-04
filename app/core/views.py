from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Log, Notification


class LogList(ListView):
    template_name = 'core/log_list.html'
    model = Log
    context_object_name = 'logs'


class LogUpdate(UpdateView):
    template_name = 'core/form.html'
    model = Log
    fields = ['user', 'event', 'eventDescription']
    success_url = '/core/log/list/'


class LogCreate(CreateView):
    model = Log
    template_name = 'core/form.html'
    fields = ['user', 'event', 'eventDescription']
    success_url = '/core/log/list/'


class LogDelete(DeleteView):
    model = Log
    template_name = 'core/confirm_delete.html'
    success_url = '/core/log/list/'


class NotificationList(ListView):
    template_name = 'core/notification_list.html'
    model = Notification
    context_object_name = 'notifications'


class NotificationUpdate(UpdateView):
    template_name = 'core/form.html'
    model = Notification
    fields = ['user', 'description', 'style']
    success_url = '/core/notification/list/'


class NotificationCreate(CreateView):
    model = Notification
    template_name = 'core/form.html'
    fields = ['user', 'description', 'style']
    success_url = '/core/notification/list/'


class NotificationDelete(DeleteView):
    model = Notification
    template_name = 'core/confirm_delete.html'
    success_url = '/core/notification/list/'
