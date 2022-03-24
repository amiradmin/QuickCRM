from django.shortcuts import render
from exam_certification.models import CertificateType
from django.contrib.auth.mixins import LoginRequiredMixin
from authorization.sidebarmixin import SidebarMixin
from django.views.generic import View, TemplateView
# Create your views here.

class CertificateTypeView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "certificates/cer_type.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CertificateTypeView, self).get_context_data()
        certificateType = CertificateType.objects.all()
        context['certificateType'] = certificateType
        return context
