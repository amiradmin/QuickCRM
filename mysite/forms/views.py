from django.shortcuts import render
from django.views.generic import View,TemplateView
# Create your views here.



class NewForm(TemplateView):

    template_name = "forms/new_form.html"

    def get_context_data(self):
        context = super(NewForm, self).get_context_data()
        # form = MedicineForm()
        # context['form'] = form
        return context