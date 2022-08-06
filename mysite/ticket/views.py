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


class ArticleUpdateView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = 'ticket/update_ticket.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleUpdateView, self).get_context_data()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] = candidate
        return context

    def post(self, request, *args, **kwargs):
        context = super(ArticleUpdateView, self).get_context_data()
        obj = Ticket.objects.filter(id=self.kwargs['id']).first()
        if obj.archived :
            obj.archived = False
            obj.status = 'On Process'
        else:
            obj.archived = True
            obj.status = 'Done'


        obj.save()

        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] = candidate
        # return context
        return redirect('ticket:allticket_')



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
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
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
            obj.message = request.POST['message']
            if request.FILES.get('file1', False):
                obj.fileOne = request.FILES['file1']
            if request.FILES.get('file2', False):
                obj.fileTwo = request.FILES['file2']
            obj.status='new'
            obj.save()


            return redirect('accounting:canprofile_',id=candidate.id,status=False)


class DeleteTicketView(SidebarMixin, LoginRequiredMixin,DeleteView):
    model = Ticket
    success_url = reverse_lazy('ticket:allticket_')


class TicketListView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "ticket/all_ticket.html"

    def get_context_data(self):
        context = super(TicketListView, self).get_context_data()
        tickets = Ticket.objects.filter(archived=False).order_by('-id')
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] =candidate
        context['tickets'] = tickets
        # context['candidate'] = tickets

        return context


class CandidateAllTicketListView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "ticket/all_candidate_ticket.html"

    def get_context_data(self):
        context = super(CandidateAllTicketListView, self).get_context_data()

        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        tickets = Ticket.objects.filter(candidate=candidate).order_by('-id')
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] =candidate
        context['tickets'] = tickets
        # context['candidate'] = tickets

        return context


class CandidateAllTicketView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "ticket/candidate_all_ticket.html"

    def get_context_data(self,id):
        context = super(CandidateAllTicketView, self).get_context_data()
        candidate=TesCandidate.objects.filter(id=self.kwargs['id']).first()
        # tickets = Ticket.objects.filter(candidate=candidate).order_by('-id')
        contacts = Contact.objects.filter(Q(candidate=candidate) & Q(readFlag=False))
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        # if contact.count() > 0:
        #     context['newMessage'] = True
        # else:
        #     context['newMessage'] = False
        # context['tickets'] = tickets
        context['candidate'] = candidate
        context['contacts'] = contacts
        context['group_name'] = group_name

        return context

class HistoryTicketView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "ticket/history.html"

    def get_context_data(self,id):
        context = super(HistoryTicketView, self).get_context_data()
        ticket = Ticket.objects.filter(id=self.kwargs['id']).first()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        if group_name is not 'candidates':
            ticket.status= 'OnProcess'
            ticket.save()
        context['group_name'] = group_name
        context['candidate'] =candidate
        context['ticket'] = ticket
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            obj = TicketAnswer()
            obj.message = request.POST['answer_message']
            obj.status='new'
            obj.save()

            ticketObj = Ticket.objects.filter(id=self.kwargs['id']).first()
            ticketObj.answer.add(obj)
            # ticketObj.save()
            group_name = self.request.user.groups.values_list('name', flat=True).first()
            if group_name == 'candidates':
                return redirect('ticket:candidateallticket_')
            else:
                return redirect('ticket:allticket_')


class AnswerTicketView(LoginRequiredMixin,TemplateView):
    template_name = "ticket/ticket_answer.html"
    def get_context_data(self,id):
        context = super(AnswerTicketView, self).get_context_data()
        ticket = Ticket.objects.filter(id=self.kwargs['id']).first()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] =candidate
        context['ticket'] = ticket
        return context
    def post(self, request, *args, **kwargs):
        context = super(AnswerTicketView, self).get_context_data()
        print('here now')
        if request.method == 'POST':
            obj = TicketAnswer()
            obj.message = request.POST['message']

            obj.status='new'
            if request.FILES.get('file1', False):
                obj.fileOne = request.FILES['file1']
            if request.FILES.get('file2', False):
                obj.fileTwo = request.FILES['file2']
            obj.save()

            ticketObj = Ticket.objects.filter(id=self.kwargs['id']).first()
            ticketObj.answer.add(obj)
            ticketObj.save()
            # sendMail("amirbehvandi747@gmail.com")
            candidate = TesCandidate.objects.filter(user=self.request.user).first()
            group_name = self.request.user.groups.values_list('name', flat=True).first()
            context['group_name'] = group_name
            context['candidate'] = candidate
            print(group_name)

        return redirect('ticket:allticket_')

class ArchivedTicketListView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "ticket/all_ticket.html"

    def get_context_data(self):
        context = super(ArchivedTicketListView, self).get_context_data()
        tickets = Ticket.objects.filter(archived=True)
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] =candidate
        context['tickets'] = tickets

        return context