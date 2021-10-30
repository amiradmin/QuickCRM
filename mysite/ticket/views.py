from django.shortcuts import render,redirect
from ticket.models import Ticket,TicketAnswer
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
            lastTicket=Ticket.objects.last()
            if lastTicket:
                ticketNumber = lastTicket.id
                ticketNumber+=1
            else:
                ticketNumber = 0

            obj = Ticket()
            candidate = TesCandidate.objects.filter(id=candidate.id).first()
            obj.candidate = candidate
            obj.title = request.POST['title']
            obj.TicketNumber ="TESTIK-"+ str(ticketNumber)
            obj.department = request.POST['department']
            obj.message = request.POST['message']
            obj.status='new'
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



class HistoryTicketView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "ticket/history.html"

    def get_context_data(self,id):
        context = super(HistoryTicketView, self).get_context_data()
        ticket = Ticket.objects.filter(id=self.kwargs['id']).first()
        context['ticket'] = ticket

        return context


class AnswerTicketView(LoginRequiredMixin,TemplateView):
    template_name = "ticket/ticket_answer.html"

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            obj = TicketAnswer()
            obj.title = request.POST['title']
            obj.message = request.POST['message']
            obj.status='new'
            obj.save()

            ticketObj = Ticket.objects.filter(id=self.kwargs['id']).first()
            ticketObj.answer.add(obj)

            # sendMail("amirbehvandi747@gmail.com")

            return redirect('ticket:allticket_')