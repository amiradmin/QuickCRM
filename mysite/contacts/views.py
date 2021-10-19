from django.shortcuts import render,redirect
from contacts.models import Contact
from django.views.generic import View,TemplateView
from training.models import TesCandidate
from django.contrib.auth.mixins import LoginRequiredMixin
from contacts.models import Contact
from  authorization.sidebarmixin import SidebarMixin
# Create your views here.

class NewContactView(LoginRequiredMixin,TemplateView):
    template_name = "contact/new_contact.html"

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            obj = Contact()
            candidate = TesCandidate.objects.filter(id=1054237).first()
            obj.candidate = candidate
            obj.type = 'Candidate'
            obj.messageType = 'Message'
            obj.department = request.POST['department']
            obj.message = request.POST['message']

            # lecturer = Lecturer.objects.filter(id=self.kwargs['id']).first()
            # lecturer.aboutMe = aboutMe
            obj.save()
            return redirect('accounting:canprofile_',id=1054237)


class MessageListView(LoginRequiredMixin,TemplateView):
    template_name = "contact/message_list.html"

    def get_context_data(self):
        context = super(MessageListView, self).get_context_data()
        candidate = TesCandidate.objects.filter(id=1054237).first()
        message_list = Contact.objects.filter(candidate=candidate )
        context['message_list'] = message_list

        return context

class AdminMessageListView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "contact/admin_message_list.html"

    def get_context_data(self):
        context = super(AdminMessageListView, self).get_context_data()
        message_list = Contact.objects.filter(type="Candidate").order_by('-id')
        context['message_list'] = message_list
        return context

class AdminOutboxView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "contact/admin_message_list.html"

    def get_context_data(self):
        context = super(AdminOutboxView, self).get_context_data()
        message_list = Contact.objects.filter(type="Admin").order_by('-id')
        context['message_list'] = message_list
        return context

class MessageDetailView(LoginRequiredMixin,TemplateView):
    template_name = "contact/message_detail.html"

    def get_context_data(self,id):
        context = super(MessageDetailView, self).get_context_data()
        message = Contact.objects.filter(id=self.kwargs['id']).first()
        context['message'] = message

        return context