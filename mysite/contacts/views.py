from django.shortcuts import render,redirect
from contacts.models import Contact
from django.views.generic import View,TemplateView
from training.models import TesCandidate,Event
from django.contrib.auth.mixins import LoginRequiredMixin
from contacts.models import Contact
from  authorization.sidebarmixin import SidebarMixin
from django.db.models import Q
import datetime
from mailer.views import sendMail
from forms.models import CandidateForms
# Create your views here.

class NewContactView(LoginRequiredMixin,TemplateView):
    template_name = "contact/new_contact.html"
    def get_context_data(self, *args, **kwargs):
        context = super(NewContactView, self).get_context_data()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        context['candidate'] =candidate

        return context

    def post(self, request, *args, **kwargs):
        context = super(NewContactView, self).get_context_data()
        if request.method == 'POST':
            candidate = TesCandidate.objects.filter(id=self.kwargs['id']).first()
            obj = Contact()
            candidate = TesCandidate.objects.filter(id=candidate.id).first()

            obj.candidate = candidate
            obj.type = 'Candidate'
            obj.messageType = 'Message'
            obj.formName = candidate.email
            group_name = self.request.user.groups.values_list('name', flat=True).first()
            obj.department = request.POST['department']
            obj.message = request.POST['message']
            obj.save()
            # sendMail("amirbehvandi747@gmail.com")
            context['group_name'] = group_name
            context['candidate'] = candidate
            return redirect('accounting:canprofile_',id=candidate.id)




class AdminNewContactView(LoginRequiredMixin,TemplateView):
    template_name = "contact/admin_new_contact.html"

    def get_context_data(self):
        context = super(AdminNewContactView, self).get_context_data()
        candidates = TesCandidate.objects.all().order_by('first_name')
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidates'] = candidates
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        context['candidate'] =candidate

        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            obj = Contact()
            candidate = TesCandidate.objects.filter(id=request.POST['candidateID'].split('-')[0]).first()
            obj.candidate = candidate
            obj.type = 'Admin'
            obj.messageType = 'Message'
            obj.department = request.POST['department']
            obj.message = request.POST['message']
            obj.save()
            return redirect('training:trainpanel_')


class MessageListView(LoginRequiredMixin,TemplateView):
    template_name = "contact/message_list.html"

    def get_context_data(self,id):
        context = super(MessageListView, self).get_context_data()

        candidate = TesCandidate.objects.filter(id = self.kwargs['id']).first()
        events = Event.objects.filter(candidate = candidate)
        contact = Contact.objects.filter(candidate=candidate).order_by("-id")
        contactRead = Contact.objects.filter(Q(candidate=candidate)|Q(readFlag=True)).count()
        message_list = Contact.objects.filter(candidate=candidate)

        if message_list.count() > 0 :
            for item in message_list:
                item.readFlag = True
                item.save()

        now = datetime.datetime.now()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] = candidate
        context['events'] = events
        context['now'] = now
        context['contact'] = contact
        context['contactRead'] = contactRead
        context['message_list'] = message_list

        return context

class AdminMessageListView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "contact/admin_message_list.html"

    def get_context_data(self):
        context = super(AdminMessageListView, self).get_context_data()
        message_list = Contact.objects.filter(Q(type="Candidate") | Q(type="Site")).order_by('-id')
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] =candidate
        context['message_list'] = message_list
        return context

class AdminOutboxView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "contact/admin_message_list.html"

    def get_context_data(self):
        context = super(AdminOutboxView, self).get_context_data()
        message_list = Contact.objects.filter(type="Admin").order_by('-id')
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] =candidate
        context['message_list'] = message_list
        return context


class CandidateOutboxView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "contact/admin_message_list.html"

    def get_context_data(self):
        context = super(CandidateOutboxView, self).get_context_data()
        print("Here")
        candidate = TesCandidate.objects.filter(user = self.request.user).first()
        message_list = Contact.objects.filter(candidate=candidate ).filter(type="Candidate").order_by('-id')

        # candidate = TesCandidate.objects.filter(id=self.kwargs['id']).first()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        context['candidate'] =candidate
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['message_list'] = message_list
        context['candidate'] = candidate
        return context

class MessageDetailView(LoginRequiredMixin,TemplateView):
    template_name = "contact/message_detail.html"

    def get_context_data(self,id):
        context = super(MessageDetailView, self).get_context_data()
        message = Contact.objects.filter(id=self.kwargs['id']).first()
        message.readFlag=True
        message.save()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        context['candidate'] =candidate
        context['message'] = message

        return context

class AdminArchivedView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "contact/admin_message_list.html"

    def get_context_data(self):
        context = super(AdminArchivedView, self).get_context_data()
        message_list = Contact.objects.filter(archived=True).order_by('-id')
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        group_name = self.request.user.groups.values_list('name', flat=True).first()
        context['group_name'] = group_name
        context['candidate'] =candidate
        context['message_list'] = message_list
        return context