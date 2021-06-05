from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from training.models import Event,CandidateProfile,Country,Location,Product,Lecturer
from django.contrib.auth.models import User
import time
import datetime
# Create your views here.


class CandidatelListView(TemplateView):
    template_name = "training/candidate_table.html"

    def get_context_data(self):
        context = super(CandidatelListView, self).get_context_data()
        can_list = CandidateProfile.objects.all()
        context['can_list'] = can_list
        return context
    
class NewCandidatelView(TemplateView):
    template_name = "training/new_candidate.html"



    def post(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'POST':
            print('OK')
            user = User()
            user.candidateprofile.first_name = request.POST['first_name']
            user.candidateprofile.last_name = request.POST['last_name']
            user.candidateprofile.twi_candidate_id = request.POST['twi_candidate_id']
            user.candidateprofile.customer_id = request.POST['customer_id']
            user.candidateprofile.address = request.POST['address']
            user.candidateprofile.passport_id = request.POST['passport_id']
            user.candidateprofile.sponsor_company = request.POST['sponsor_company']
            user.candidateprofile.email = request.POST['email']
            user.candidateprofile.city = request.POST['city']
            user.candidateprofile.country = request.POST['country']
            user.candidateprofile.contact_number = request.POST['contact_number']
            user.candidateprofile.note = request.POST['note']
            if request.FILES.get('photo', False):
                user.candidateprofile.photo = request.FILES['photo']
            if request.FILES.get('document_1', False):
                user.candidateprofile.document_1 = request.FILES['document_1']
            if request.FILES.get('document_2', False):
                user.candidateprofile.document_2 = request.FILES['document_2']
            if request.FILES.get('document_3', False):
                user.candidateprofile.document_3 = request.FILES['document_3']
            if request.FILES.get('document_4', False):
                user.candidateprofile.document_4 = request.FILES['document_4']
            if request.FILES.get('document_5', False):
                user.candidateprofile.document_5 = request.FILES['document_5']
            if request.FILES.get('document_6', False):
                user.candidateprofile.document_6 = request.FILES['document_6']
            if request.FILES.get('document_7', False):
                user.candidateprofile.document_7 = request.FILES['document_7']
            if request.FILES.get('document_8', False):
                user.candidateprofile.document_8 = request.FILES['document_8']
            if request.FILES.get('document_9', False):
                user.candidateprofile.document_9 = request.FILES['document_9']
            user.save() 
        return redirect('training:canprofile_')


class UpdateCandidatelView(TemplateView):
    template_name = "training/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateCandidatelView, self).get_context_data()
        can = CandidateProfile.objects.filter(id = self.kwargs['id']).first()
        context['can'] = can

        return context

    def put(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'POST':
            print('OK')
            user = User()
            user.username = request.POST['username']
            user.last_name = request.POST['last_name']
            user.password = request.POST['password']
            user.save()
            user.candidateprofile.first_name = request.POST['first_name']
            user.candidateprofile.last_name = request.POST['last_name']
            user.candidateprofile.twi_candidate_id = request.POST['twi_candidate_id']
            user.candidateprofile.customer_id = request.POST['customer_id']
            user.candidateprofile.address = request.POST['address']
            user.candidateprofile.passport_id = request.POST['passport_id']
            user.candidateprofile.sponsor_company = request.POST['sponsor_company']
            user.candidateprofile.email = request.POST['email']
            user.candidateprofile.city = request.POST['city']
            user.candidateprofile.country = request.POST['country']
            user.candidateprofile.contact_number = request.POST['contact_number']
            user.candidateprofile.note = request.POST['note']
            if request.FILES.get('photo', False):
                user.candidateprofile.photo = request.FILES['photo']
            if request.FILES.get('document_1', False):
                user.candidateprofile.document_1 = request.FILES['document_1']
            if request.FILES.get('document_2', False):
                user.candidateprofile.document_2 = request.FILES['document_2']
            if request.FILES.get('document_3', False):
                user.candidateprofile.document_3 = request.FILES['document_3']
            if request.FILES.get('document_4', False):
                user.candidateprofile.document_4 = request.FILES['document_4']
            if request.FILES.get('document_5', False):
                user.candidateprofile.document_5 = request.FILES['document_5']
            if request.FILES.get('document_6', False):
                user.candidateprofile.document_6 = request.FILES['document_6']
            if request.FILES.get('document_7', False):
                user.candidateprofile.document_7 = request.FILES['document_7']
            if request.FILES.get('document_8', False):
                user.candidateprofile.document_8 = request.FILES['document_8']
            if request.FILES.get('document_9', False):
                user.candidateprofile.document_9 = request.FILES['document_9']
            user.save() 
        return redirect('training:canprofile_')


class DeleteCandidatelView(TemplateView):
    template_name = "training/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateCandidatelView, self).get_context_data()
        can = CandidateProfile.objects.filter(id = self.kwargs['id']).first()
        context['can'] = can

        return context

    def put(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'DELETE':

           
            return redirect('training:canprofile_')
    
    
class ProductView(TemplateView):
    template_name = "training/product_list.html"

    def get_context_data(self):
        context = super(ProductView, self).get_context_data()
        product_list = Product.objects.all()
        context['product_list'] = product_list

        return context

    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            obj = Product()
            obj.name = request.POST['name']
            obj.code = request.POST['code']
            obj.price = request.POST['price']
            obj.type = request.POST['type']
            obj.save()
        return redirect('training:product_')
    
    
class EventView(TemplateView):
    template_name = "training/event_list.html"

    def get_context_data(self):
        context = super(EventView, self).get_context_data()
        event_list = Event.objects.all()
        product_list = Product.objects.all()
        lecturers_list = Lecturer.objects.all()
        country_list = Country.objects.all()
        location_list = Location.objects.all()
        context['event_list'] = event_list
        context['product_list'] = product_list
        context['lecturers_list'] = lecturers_list
        context['country_list'] = country_list
        context['location_list'] = location_list

        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            country = Country.objects.get(id = request.POST['country'])
            product = Product.objects.get(id = request.POST['product'])
            lecturers = Lecturer.objects.get(id = request.POST['lecturer'])

            obj = Event()
            obj.name = request.POST['name']
            obj.country = country
            obj.product = product
            obj.lecturers = lecturers
            # obj.start_date = request.POST['start_date']
            
            obj.start_date = datetime.datetime.strptime(request.POST['start_date'], '%m/%d/%Y')
            obj.save()     

        return redirect('training:event_')
    
class LecturerView(TemplateView):
    template_name = "training/lecturer_list.html"

    def get_context_data(self):
        context = super(LecturerView, self).get_context_data()
        lecturer_list = Lecturer.objects.all()
        context['lecturer_list'] = lecturer_list

        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # country = Country.objects.get(id = request.POST['country'])
            obj = Lecturer()
            obj.first_name = request.POST['first_name']
            obj.last_name = request.POST['last_name']
            obj.email = request.POST['email']
            obj.mobile = request.POST['mobile']
            obj.country = request.POST['country']
            obj.city = request.POST['city']
            if request.FILES.get('photo', False):
                obj.candidateprofile.photo = request.FILES['photo']
            if request.FILES.get('document_1', False):
                obj.candidateprofile.document_1 = request.FILES['document_1']
            if request.FILES.get('document_2', False):
                obj.candidateprofile.document_2 = request.FILES['document_2']
            if request.FILES.get('document_3', False):
                obj.candidateprofile.document_3 = request.FILES['document_3']
            if request.FILES.get('document_4', False):
                user.candidateprofile.document_4 = request.FILES['document_4']
            if request.FILES.get('document_5', False):
                obj.candidateprofile.document_5 = request.FILES['document_5']
            if request.FILES.get('document_6', False):
                obj.candidateprofile.document_6 = request.FILES['document_6']
            if request.FILES.get('document_7', False):
                obj.candidateprofile.document_7 = request.FILES['document_7']
            if request.FILES.get('document_8', False):
                obj.candidateprofile.document_8 = request.FILES['document_8']
            if request.FILES.get('document_9', False):
                obj.candidateprofile.document_9 = request.FILES['document_9']
            obj.save()     

        return redirect('training:lecturer_')

class CountryView(TemplateView):
    template_name = "training/country_list.html"

    def get_context_data(self):
        context = super(CountryView, self).get_context_data()
        country_list = Country.objects.all()
        context['country_list'] = country_list

        return context

    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            obj = Country()
            obj.name = request.POST['name']
            obj.save()
        return redirect('training:country_')

class LocationView(TemplateView):
    template_name = "training/location_list.html"

    def get_context_data(self):
        context = super(LocationView, self).get_context_data()
        location_list = Location.objects.all()
        country_list = Country.objects.all()
        context['country_list'] = country_list
        context['location_list'] = location_list

        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            country = Country.objects.get(id = request.POST['country'])
            obj = Location()
            obj.name = request.POST['name']
            obj.country = country
            obj.save()     

        return redirect('training:location_')





class TrainingPanelView(TemplateView):
    template_name = "creative/layouts-vertical.html"

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
                user = User()
                user.username = request.POST['username']
                user.last_name = request.POST['last_name']
                user.password = request.POST['password']

                user.save()
                user.candidateprofile.first_name = request.POST['first_name']
                user.candidateprofile.last_name = request.POST['last_name']
                user.candidateprofile.twi_candidate_id = request.POST['twi_candidate_id']
                user.candidateprofile.customer_id = request.POST['customer_id']
                user.candidateprofile.address = request.POST['address']
                user.candidateprofile.passport_id = request.POST['passport_id']
                user.candidateprofile.sponsor_company = request.POST['sponsor_company']
                user.candidateprofile.email = request.POST['email']
                user.candidateprofile.city = request.POST['city']
                user.candidateprofile.country = request.POST['country']
                user.candidateprofile.contact_number = request.POST['contact_number']
                user.candidateprofile.note = request.POST['note']
                if request.FILES.get('photo', False):
                    user.candidateprofile.photo = request.FILES['photo']
                if request.FILES.get('document_1', False):
                    user.candidateprofile.document_1 = request.FILES['document_1']
                if request.FILES.get('document_2', False):
                    user.candidateprofile.document_2 = request.FILES['document_2']
                if request.FILES.get('document_3', False):
                    user.candidateprofile.document_3 = request.FILES['document_3']
                if request.FILES.get('document_4', False):
                    user.candidateprofile.document_4 = request.FILES['document_4']
                if request.FILES.get('document_5', False):
                    user.candidateprofile.document_5 = request.FILES['document_5']
                if request.FILES.get('document_6', False):
                    user.candidateprofile.document_6 = request.FILES['document_6']
                if request.FILES.get('document_7', False):
                    user.candidateprofile.document_7 = request.FILES['document_7']
                if request.FILES.get('document_8', False):
                    user.candidateprofile.document_8 = request.FILES['document_8']
                if request.FILES.get('document_9', False):
                    user.candidateprofile.document_9 = request.FILES['document_9']
                user.save()

            elif 'cont_btn' in request.POST:
                print('OK')
                obj = Country()
                obj.name = request.POST['name']
                obj.save()

            elif 'pro_btn' in request.POST:
                print('pro_btn')
                obj = Product()
                obj.name = request.POST['name']
                obj.code = request.POST['code']
                obj.price = request.POST['price']
                obj.save()

            elif 'loc_btn' in request.POST:
                print('location')
                print(request.POST['country'])
                country = Country.objects.get(id = request.POST['country'])
                obj = Location()
                obj.name = request.POST['name']
                obj.country = country
                obj.save()
            # return render(request, 'medicine/medicine_panel.html', {'data': response.json()})
            return redirect('training:trainpanel_')
