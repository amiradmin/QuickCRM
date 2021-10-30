from django.shortcuts import render,redirect
from ticket.models import Ticket
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View,TemplateView
from training.models import TesCandidate,Event
from mailer.views import sendMail
from  authorization.sidebarmixin import SidebarMixin
# Create your views here.

class NewTicketView(LoginRequiredMixin,TemplateView):
    template_name = "ticket/new_ticket.html"

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            candidate = TesCandidate.objects.filter(id=self.kwargs['id']).first()
            obj = Ticket()
            candidate = TesCandidate.objects.filter(id=candidate.id).first()
            obj.candidate = candidate
            obj.title = request.POST['title']
            obj.messageType = 'Message'
            obj.department = request.POST['department']
            obj.message = request.POST['message']
            obj.save()
            # sendMail("amirbehvandi747@gmail.com")

            return redirect('accounting:canprofile_',id=candidate.id)



class TicketListView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "ticket/all_ticket.html"

    def get_context_data(self):
        context = super(TicketListView, self).get_context_data()
        tickets = Ticket.objects.all().order_by('-id')
        context['tickets'] = tickets

        return context