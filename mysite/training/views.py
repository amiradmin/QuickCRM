from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from training.models import Event,CandidateProfile,Country,Location
from django.contrib.auth.models import User
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
        country_list = Country.objects.all()
        location_list = Location.objects.all()
        context['event_list'] = event_list
        context['country_list'] = country_list
        context['location_list'] = location_list
        return context


    def post(self, request, *args, **kwargs):

        # form = MedicineForm(self.request.POST)
        if request.method == 'POST':
            if 'new_can' in request.POST:
                print('OK')
                user = User()
                user.username = request.POST['username']
                print(request.POST['username'])
                user.password = request.POST['password']



                user.save()
                user.candidateprofile.first_name = request.POST['first_name']
                user.candidateprofile.last_name = request.POST['last_name']
                user.candidateprofile.twi_candidate_id = request.POST['twi_candidate_id']
                user.save()

            elif 'cont_btn' in request.POST:
                print('OK')
                obj = Country()
                obj.name = request.POST['name']
                obj.save()
            # return render(request, 'medicine/medicine_panel.html', {'data': response.json()})
            return redirect('training:trainpanel_')
