from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AdminPanelView(TemplateView):
    template_name = "adminpanel.html"

    def get_context_data(self):
        context = super(AdminPanelView, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context
