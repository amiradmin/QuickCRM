from django.shortcuts import render, redirect
from exam_certification.models import CertificateAttendance
from django.contrib.auth.mixins import LoginRequiredMixin
from authorization.sidebarmixin import SidebarMixin
from django.views.generic import View, TemplateView
from training.models import TesCandidate,Event
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
import datetime
# Create your views here.

class CertificateAttendanceView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/cer_attendance.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CertificateAttendanceView, self).get_context_data()
        # certificateType = CertificateType.objects.all()
        # context['certificateType'] = certificateType
        return context

class FinalCertificateAttendanceView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/certificate_of_attendance.html"

    def get_context_data(self, *args, **kwargs):
        context = super(FinalCertificateAttendanceView, self).get_context_data()
        candidate = TesCandidate.objects.filter(id=self.kwargs['canID']).first()
        event = Event.objects.filter(id=self.kwargs['eventID']).first()
        form = CertificateAttendance.objects.filter(Q(candidate=candidate) & Q(event=event)).first()
        print(form)
        context['form'] = form
        return context
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print('uploadFormBack')
            candidate = TesCandidate.objects.filter(id=self.kwargs['canID']).first()
            event = Event.objects.filter(id=self.kwargs['eventID']).first()
            obj = CertificateAttendance.objects.filter(Q(candidate=candidate) & Q(event=event)).first()
            obj.file = request.FILES['pdfFile']
            obj.save()
        return redirect('exam_certification:cersummary_')

class NewCertificateAttendance(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/new_attendance.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewCertificateAttendance, self).get_context_data()
        candidates = TesCandidate.objects.all()
        events = Event.objects.all()
        context['candidates'] = candidates
        context['events'] = events
        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':

            print("Form was sent!")
            candidate = TesCandidate.objects.filter(id=self.request.POST['candidate']).first()
            event = Event.objects.filter(id=self.request.POST['event']).first()
            if CertificateAttendance.objects.filter(Q(candidate=candidate) & Q(event=event)).exists:
                obj = CertificateAttendance.objects.filter(Q(candidate=candidate) & Q(event=event)).first()
                obj.candidate = candidate
                obj.event = event
                obj.name = candidate.first_name + " " + candidate.last_name
                obj.authorized_signatory = self.request.POST['authorized_signatory']
                obj.course_duration = self.request.POST['course_duration']
                obj.certiﬁcate_number = self.request.POST['certiﬁcate_number']
                obj.issue_date = datetime.datetime.strptime(self.request.POST['issue_date'], '%m/%d/%Y')
                obj.save()
            else:
                obj = CertificateAttendance()
                obj.candidate = candidate
                obj.event = event
                obj.name = candidate.first_name + " " + candidate.last_name
                obj.authorized_signatory = self.request.POST['authorized_signatory']
                obj.course_duration = self.request.POST['course_duration']
                obj.certiﬁcate_number = self.request.POST['certiﬁcate_number']
                obj.issue_date = datetime.datetime.strptime(self.request.POST['issue_date'], '%m/%d/%Y')
                obj.save()

        return redirect('exam_certification:cersummary_')


class DeleteCertificateAttendance(SidebarMixin, LoginRequiredMixin, DeleteView):
    model = CertificateAttendance
    success_url = reverse_lazy('exam_certification:cersummary_')

class CertificateSummayView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/cer_summary.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CertificateSummayView, self).get_context_data()
        certificateAttendances = CertificateAttendance.objects.all()
        context['certificateAttendances'] = certificateAttendances
        return context
