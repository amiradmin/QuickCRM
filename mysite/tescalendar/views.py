from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from training.models import Event,CandidateProfile,Country,Location,Product,Lecturer
from django.contrib.auth.models import User
import time
import datetime




class CalendarView(TemplateView):
    template_name = "calendar/apps-calendar.html"

    def get_context_data(self):
        context = super(CalendarView, self).get_context_data()
        event_list = Event.objects.all()
        context['event_list'] = event_list
        return context