from django.shortcuts import render,redirect
from ticket.models import Ticket,TicketAnswer
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View,TemplateView
from training.models import TesCandidate,Event
from mailer.views import sendMail
from  authorization.sidebarmixin import SidebarMixin
from training.models import TesCandidate
from django.views.generic import UpdateView
from django.shortcuts import render,redirect
from django.views.generic.edit import DeleteView
from contacts.models import Contact
from django.db.models import Q
from django.urls import reverse_lazy
from django.urls import reverse
from staff.models import Staff
import datetime
# Create your views here.


class ArticleUpdateView(UpdateView):
    model = Ticket
    template_name = 'ticket/update_ticket.html'
    success_message = 'Ticket has archived successfully'
    fields = ()

    def get_success_url(self):
        return reverse('ticket:archivedtickets_')


    def get_object(self, queryset=None):
        obj = super(ArticleUpdateView, self).get_object(queryset)
        obj.archived = True
        obj.save()

        return obj




class AssignToUpdateView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = 'ticket/asigned_ticket.html'

    def get_context_data(self,id):
        context = super(AssignToUpdateView, self).get_context_data()
        staffs = Staff.objects.all()
        context['staffs'] = staffs
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            staff=Staff.objects.filter(id=request.POST['staff']).first()
            obj = Ticket.objects.filter(id=self.kwargs['id']).first()
            obj.asignedTo = staff
            obj.save()

            # if staff.email:
            print(staff.email)
            fullname=staff.first_name + " " + staff.last_name
            msg="The ticket with number "+ obj.TicketNumber + " has been assigned to you!"
            sendMail(staff.email,fullname,msg)


            return redirect('ticket:allticket_')


class NewTicketView(LoginRequiredMixin,TemplateView):
    template_name = "ticket/new_ticket.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewTicketView, self).get_context_data()
        print(self.kwargs['id'])
        candidate = TesCandidate.objects.filter(id = self.kwargs['id']).first()
        events = Event.objects.filter(candidate = candidate)
        contact = Contact.objects.filter(Q(candidate=candidate) & Q(readFlag=False)).order_by("-id")
        contactRead = Contact.objects.filter(Q(candidate=candidate) & Q(readFlag=False))
        print(contactRead)
        now = datetime.datetime.now()
        contact = Contact.objects.filter(Q(candidate=candidate) & Q(readFlag=False))
        if contact.count() > 0:
            context['newMessage'] = True
        else:
            context['newMessage'] = False
        context['candidate'] = candidate
        context['events'] = events
        context['now'] = now
        context['contact'] = contact
        context['contactRead'] = contactRead
        return context

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
            if candidate.email:
                print(candidate.email)
                fullname=candidate.first_name + " " + candidate.last_name
                msg="Your ticket with number "+ obj.TicketNumber +" has been created!"
                sendMail(candidate.email,fullname,msg)

            fullname=candidate.first_name + " " + candidate.last_name
            msg="ticket with number "+ obj.TicketNumber +" has been created!"
            sendMail('registration@tescan.ca',fullname,msg)

            return redirect('accounting:canprofile_',id=candidate.id)


class DeleteTicketView(SidebarMixin, LoginRequiredMixin,DeleteView):
    model = Ticket
    success_url = reverse_lazy('ticket:allticket_')


class TicketListView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "ticket/all_ticket.html"

    def get_context_data(self):
        context = super(TicketListView, self).get_context_data()
        tickets = Ticket.objects.filter(archived=False).order_by('-id')
        candidate = TesCandidate.objects.filter(id=self.kwargs['id']).first()
        context['tickets'] = tickets
        context['candidate'] = tickets

        return context

class CandidateAllTicketView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "ticket/candidate_all_ticket.html"

    def get_context_data(self,id):
        context = super(CandidateAllTicketView, self).get_context_data()
        candidate=TesCandidate.objects.filter(id=self.kwargs['id']).first()
        tickets = Ticket.objects.filter(candidate=candidate).order_by('-id')
        contact = Contact.objects.filter(Q(candidate=candidate) & Q(readFlag=False))
        if contact.count() > 0:
            context['newMessage'] = True
        else:
            context['newMessage'] = False
        context['tickets'] = tickets
        context['candidate'] = candidate

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

class ArchivedTicketListView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "ticket/all_ticket.html"

    def get_context_data(self):
        context = super(ArchivedTicketListView, self).get_context_data()
        tickets = Ticket.objects.filter(archived=True)
        context['tickets'] = tickets

        return context