from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse

from .models import Ticket, User
from .forms import AddTicketForm
# class MyView(View):
#
#     def get(self, request, *args, **kwargs):
#         return HttpResponse("Не знаю зачем я это написал")
#
# class MyTemplateView(TemplateView):
#     template_name = "ticket/add-ticket.html"
#
#     def get_context_data(self, **kwargs):
#         context = super(MyTemplateView, self).get_context_data(**kwargs)
#         context["text"] = "Hi world"
#         return context

class AddTicket(CreateView):
    """Add ticket"""
    model = Ticket
    form_class = AddTicketForm
    template_name = 'ticket/add-ticket.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/ticket/add-ticket/')

    def success_url(self):
        return redirect("/add-ticket/")

class ListTicket(ListView):
    """Список тикетов пользователя"""
    model = Ticket
    #queryset = Ticket.objects.all()
    context_object_name = "tickets"
    template_name = "ticket/list_ticket.html"

    def queryset(self):
        return Ticket.objects.filter(user=self.request.user)

class UpdateTicket(UpdateView):
    """Редактирование тикета"""
    model = Ticket
    form = AddTicketForm
    fields = fields = ('category','title', 'text')
    template_name = "ticket/update-ticket.html"

    def get_success_url(self):
        return reverse('list-ticket')
