from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class CandidateProfileView(TemplateView):
    template_name = "teachers-singel.html"

    def get_context_data(self):
        context = super(CandidateProfileView, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context


class TrainingPanelView(TemplateView):
    template_name = "trainingpanel.html"

    def get_context_data(self):
        context = super(TrainingPanelView, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context
