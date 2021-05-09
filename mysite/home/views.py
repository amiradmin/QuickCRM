from django.shortcuts import render,redirect
from django.views.generic import TemplateView

# Create your views here.



class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super(HomeView, self).get_context_data()

        # form = MedicineForm()
        # context['event_list'] = event_list
        return context
