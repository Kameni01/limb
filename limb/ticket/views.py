from django.shortcuts import render
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Ticket

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
