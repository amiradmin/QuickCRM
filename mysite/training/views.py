from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from training.models import Event
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
        event_list = Event.objects.all()
        context['event_list'] = event_list
        return context


    def post(self, request, *args, **kwargs):

        # form = MedicineForm(self.request.POST)
        if request.method == 'POST':
            if 'new_can' in request.POST:
                print('OK')



        # return render(request, 'medicine/medicine_panel.html', {'data': response.json()})
            return redirect('training:trainpanel_')
