from django.shortcuts import render
from django.views.generic import TemplateView
from training.models import Event,Location
# Create your views here.


class MapView(TemplateView):
    template_name = "training/map.html"

    def get_context_data(self):
        context = super(MapView, self).get_context_data()
        event_list = Event.objects.select_related('location').all()
        context['event_list'] = event_list
        print(event_list)

        return context
