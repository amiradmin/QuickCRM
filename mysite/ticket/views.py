from django.shortcuts import render,redirect
from ticket.models import Ticket,TicketAnswer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View,TemplateView
from training.models import TesCandidate,Event
from mailer.views import sendMail
from  authorization.sidebarmixin import SidebarMixin
from training.models import TesCandidate
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
            if request.FILES.get('file1', False):
                obj.fileOne = request.FILES['file1']
            if request.FILES.get('file2', False):
                obj.fileTwo = request.FILES['file2']
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

class CandidateAllTicketView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "ticket/candidate_all_ticket.html"

    def get_context_data(self,id):
        context = super(CandidateAllTicketView, self).get_context_data()
        candidate=TesCandidate.objects.filter(id=self.kwargs['id']).first()
        tickets = Ticket.objects.filter(candidate=candidate).order_by('-id')
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
            obj.asignedTo = request.POST['asignedTo']
            obj.status='new'
            if request.FILES.get('file1', False):
                obj.fileOne = request.FILES['file1']
            if request.FILES.get('file2', False):
                obj.fileTwo = request.FILES['file2']
            obj.save()

            ticketObj = Ticket.objects.filter(id=self.kwargs['id']).first()
            ticketObj.answer.add(obj)
            ticketObj.asignedTo = request.POST['asignedTo']
            ticketObj.save()
            # sendMail("amirbehvandi747@gmail.com")

            return redirect('ticket:allticket_')