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
        can_list = CandidateProfile.objects.all().order_by("-id")
        context['can_list'] = can_list
        return context
    
class NewCandidatelView(TemplateView):
    template_name = "training/new_candidate.html"



    def post(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'POST':
            print('OK')
            user = CandidateProfile()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.tes_candidate_id = request.POST['tes_id']
            user.customer_id = request.POST['customer_id']
            user.address = request.POST['address']
            # user.passport_id = request.POST['passport_id']
            user.sponsor_company = request.POST['sponsor_company']
            user.email = request.POST['email']
            user.city = request.POST['city']
            user.country = request.POST['country']
            user.contact_number = request.POST['phone']
            # user.note = request.POST['note']
            if request.FILES.get('photo', False):
                user.photo = request.FILES['photo']
            if request.FILES.get('doc_1', False):
                user.document_1 = request.FILES['doc_1']
            if request.FILES.get('doc_2', False):
                user.document_2 = request.FILES['doc_2']
            if request.FILES.get('doc_3', False):
                user.document_3 = request.FILES['doc_3']
            if request.FILES.get('doc_4', False):
                user.document_4 = request.FILES['doc_4']
            if request.FILES.get('doc_5', False):
                user.document_5 = request.FILES['doc_5']
            if request.FILES.get('doc_6', False):
                user.document_6 = request.FILES['doc_6']
            if request.FILES.get('doc_7', False):
                user.document_7 = request.FILES['doc_7']
            if request.FILES.get('doc_8', False):
                user.document_8 = request.FILES['doc_8']
            if request.FILES.get('doc_9', False):
                user.document_9 = request.FILES['doc_9']
            if request.FILES.get('doc_10', False):
                user.document_9 = request.FILES['doc_10']
            user.save() 
        return redirect('training:canlist_')


class UpdateCandidatelView(TemplateView):
    template_name = "training/update_candidate.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateCandidatelView, self).get_context_data()
        can = CandidateProfile.objects.filter(id = self.kwargs['id']).first()
        context['can'] = can

        return context

    def post(self, request, *args, **kwargs):
        print('OK')
        # form = MedicineForm(self.request.POST)
        if request.method == 'POST':
            print('OK')
            
            user = CandidateProfile.objects.filter(id = self.kwargs['id']).first()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.tes_candidate_id = request.POST['tes_id']
            user.customer_id = request.POST['customer_id']
            user.address = request.POST['address']
            # user.passport_id = request.POST['passport_id']
            user.sponsor_company = request.POST['sponsor_company']
            user.email = request.POST['email']
            user.city = request.POST['city']
            user.country = request.POST['country']
            user.contact_number = request.POST['phone']
            # user.note = request.POST['note']
            if request.FILES.get('photo', False):
                user.photo = request.FILES['photo']
            if request.FILES.get('doc_1', False):
                user.document_1 = request.FILES['doc_1']
            if request.FILES.get('doc_2', False):
                user.document_2 = request.FILES['doc_2']
            if request.FILES.get('doc_3', False):
                user.document_3 = request.FILES['doc_3']
            if request.FILES.get('doc_4', False):
                user.document_4 = request.FILES['doc_4']
            if request.FILES.get('doc_5', False):
                user.document_5 = request.FILES['doc_5']
            if request.FILES.get('doc_6', False):
                user.document_6 = request.FILES['doc_6']
            if request.FILES.get('doc_7', False):
                user.document_7 = request.FILES['doc_7']
            if request.FILES.get('doc_8', False):
                user.document_8 = request.FILES['doc_8']
            if request.FILES.get('doc_9', False):
                user.document_9 = request.FILES['doc_9']
            user.save() 
        return redirect('training:canlist_')


class DeleteCandidatelView(TemplateView):
    template_name = "training/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DeleteCandidatelView, self).get_context_data()
        can = CandidateProfile.objects.filter(id = self.kwargs['id']).first()
        context['can'] = can

        return context

    def get(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'GET':
            print('Del Here')
            can = CandidateProfile.objects.filter(id = self.kwargs['id']).first()
            print(can.first_name)
            can.delete()
            return redirect('training:canlist_')
    
    
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


    
class UpdateProductView(TemplateView):
    template_name = "training/update_product.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateProductView, self).get_context_data()
        product = Product.objects.filter(id = self.kwargs['id']).first()
        context['product'] = product
        return context

    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            obj = Product.objects.filter(id = self.kwargs['id']).first()
            obj.name = request.POST['name']
            obj.code = request.POST['code']
            obj.price = request.POST['price']
            obj.type = request.POST['type']
            obj.save()
        return redirect('training:product_')



class DeleteProductView(TemplateView):
    template_name = "training/update.html"



    def get(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'GET':
            print('Del Here')
            product = Product.objects.filter(id = self.kwargs['id']).first()
            print(product.name)
            product.delete()
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
            location = Location.objects.get(id = request.POST['location'])

            obj = Event()
            obj.name = request.POST['name']
            obj.country = country
            obj.product = product
            obj.lecturers = lecturers
            obj.location = location
            # obj.start_date = request.POST['start_date']
            
            obj.start_date = datetime.datetime.strptime(request.POST['start_date'], '%m/%d/%Y')
            obj.save()     

        return redirect('training:event_')

class UpdateEventView(TemplateView):
    template_name = "training/update_event.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateEventView, self).get_context_data()
        event = Event.objects.filter(id = self.kwargs['id']).first()
        product_list = Product.objects.all()
        lecturers_list = Lecturer.objects.all()
        country_list = Country.objects.all()
        location_list = Location.objects.all()
        context['event'] = event
        context['product_list'] = product_list
        context['lecturers_list'] = lecturers_list
        context['country_list'] = country_list
        context['location_list'] = location_list

        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            print(request.POST['country'])
            country = Country.objects.get(id = request.POST['country'])
            product = Product.objects.get(id = request.POST['product'])
            lecturers = Lecturer.objects.get(id = request.POST['lecturer'])
            location = Location.objects.get(id = request.POST['location'])

            obj = Event.objects.filter(id = self.kwargs['id']).first()
            obj.name = request.POST['name']
            obj.country = country
            obj.product = product
            obj.lecturers = lecturers
            obj.location = location
            # obj.start_date = request.POST['start_date']
            
            obj.start_date = datetime.datetime.strptime(request.POST['start_date'], '%m/%d/%Y')
            obj.save()     

        return redirect('training:event_')


class DeleteEventView(TemplateView):
    template_name = "training/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DeleteEventView, self).get_context_data()
        can = Event.objects.filter(id = self.kwargs['id']).first()
        context['can'] = can

        return context

    def get(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'GET':
            print('Del Here')
            event = Event.objects.filter(id = self.kwargs['id']).first()
            print(event.name)
            event.delete()
            return redirect('training:event_')

            
class LecturerView(TemplateView):
    template_name = "training/lecturer_list.html"

    def get_context_data(self):
        context = super(LecturerView, self).get_context_data()
        lecturer_list = Lecturer.objects.all()
        context['lecturer_list'] = lecturer_list

        return context


class NewLecturerView(TemplateView):
    template_name = "training/new_lecturer.html"

    def get_context_data(self):
        context = super(NewLecturerView, self).get_context_data()
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
            obj.mobile = request.POST['phone']
            obj.country = request.POST['country']
            obj.city = request.POST['city']
            obj.address = request.POST['address']
            obj.log = request.POST['longitude']
            obj.lat = request.POST['latitude']
            if request.FILES.get('photo', False):
                obj.photo = request.FILES['photo']
            if request.FILES.get('doc_1', False):
                obj.document_1 = request.FILES['doc_1']
            if request.FILES.get('doc_2', False):
                obj.document_2 = request.FILES['doc_2']
            if request.FILES.get('doc_3', False):
                obj.document_3 = request.FILES['doc_3']
            if request.FILES.get('doc_4', False):
                obj.document_4 = request.FILES['doc_4']
            if request.FILES.get('doc_5', False):
                obj.document_5 = request.FILES['doc_5']
            if request.FILES.get('doc_6', False):
                obj.document_6 = request.FILES['doc_6']
            if request.FILES.get('doc_7', False):
                obj.document_7 = request.FILES['doc_7']
            if request.FILES.get('doc_8', False):
                obj.document_8 = request.FILES['doc_8']
            if request.FILES.get('doc_9', False):
                obj.document_9 = request.FILES['doc_9']            
            if request.FILES.get('doc_10', False):
                obj.document_10 = request.FILES['doc_10']
            obj.save()     

        return redirect('training:lecturer_')


class DeleteLecturerView(TemplateView):
    template_name = "training/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DeleteLecturerView, self).get_context_data()

        return context

    def get(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'GET':
            print('Del Here')
            lec = Lecturer.objects.filter(id = self.kwargs['id']).first()
            print(lec.first_name)
            lec.delete()
            return redirect('training:lecturer_')



class UpdateLecturerView(TemplateView):
    template_name = "training/update_lecturer.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateLecturerView, self).get_context_data()
        lecturer = Lecturer.objects.filter(id = self.kwargs['id']).first()
        context['lecturer'] = lecturer

        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # country = Country.objects.get(id = request.POST['country'])
            obj =Lecturer.objects.filter(id = self.kwargs['id']).first()
            obj.first_name = request.POST['first_name']
            obj.last_name = request.POST['last_name']
            obj.email = request.POST['email']
            obj.mobile = request.POST['phone']
            obj.country = request.POST['country']
            obj.city = request.POST['city']
            obj.address = request.POST['address']
            if request.FILES.get('photo', False):
                obj.photo = request.FILES['photo']
            if request.FILES.get('doc_1', False):
                obj.document_1 = request.FILES['doc_1']
            if request.FILES.get('doc_2', False):
                obj.document_2 = request.FILES['doc_2']
            if request.FILES.get('doc_3', False):
                obj.document_3 = request.FILES['doc_3']
            if request.FILES.get('doc_4', False):
                obj.document_4 = request.FILES['doc_4']
            if request.FILES.get('doc_5', False):
                obj.document_5 = request.FILES['doc_5']
            if request.FILES.get('doc_6', False):
                obj.document_6 = request.FILES['doc_6']
            if request.FILES.get('doc_7', False):
                obj.document_7 = request.FILES['doc_7']
            if request.FILES.get('doc_8', False):
                obj.document_8 = request.FILES['doc_8']
            if request.FILES.get('doc_9', False):
                obj.document_9 = request.FILES['doc_9']
            if request.FILES.get('doc_10', False):
                obj.document_10 = request.FILES['doc_10']
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

class DeleteCountryView(TemplateView):
    template_name = "training/update.html"



    def get(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'GET':
            print('Del Here')
            country = Country.objects.filter(id = self.kwargs['id']).first()
            print(country.name)
            country.delete()
            return redirect('training:country_')

class UpdateCountryView(TemplateView):
    template_name = "training/update_country.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateCountryView, self).get_context_data()
        country = Country.objects.filter(id = self.kwargs['id']).first()
        context['country'] = country
        return context

    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            obj = Country.objects.filter(id = self.kwargs['id']).first()
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



class UpdateLocationView(TemplateView):
    template_name = "training/update_location.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateLocationView, self).get_context_data()
        location = Location.objects.filter(id = self.kwargs['id']).first()
        context['location'] = location
        print(location.name)
        return context

    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            obj = Location.objects.filter(id = self.kwargs['id']).first()
            obj.name = request.POST['name']
            obj.log = request.POST['longitude']
            obj.lat = request.POST['latitude']
            obj.save()
        return redirect('training:location_')


class DeleteLocationView(TemplateView):
    template_name = "training/update.html"


    def get(self, request, *args, **kwargs):
        # form = MedicineForm(self.request.POST)
        if request.method == 'GET':
            print('Del Here')
            loc = Location.objects.filter(id = self.kwargs['id']).first()
            
            loc.delete()
            return redirect('training:location_')

class TrainingPanelView(TemplateView):
    template_name = "training/layouts-vertical.html"

    def get_context_data(self):
        context = super(TrainingPanelView, self).get_context_data()
        event_list = Event.objects.all()
        canCount = CandidateProfile.objects.count()
        lecCount = Lecturer.objects.count()
        product = Product.objects.all()
      
        context['event_list'] = event_list
        context['eventCount'] = event_list.count()
        context['canCount'] = canCount
        context['lecCount'] = lecCount
        context['product'] = product
        context['proCount'] = product.count()

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
