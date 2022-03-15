from django.shortcuts import render
from django.views.generic import View, TemplateView
from authorization.sidebarmixin import SidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
class TaskSchedulerReport(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "scheduler/sch.html"

    def get_context_data(self, *args, **kwargs):
        print("Amir Task")
        context = super(TaskSchedulerReport, self).get_context_data()

        context['report'] = 'Hello'
        return context


