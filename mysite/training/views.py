from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from training.models import Event,Country,Location,Product,Lecturer,TesCandidate,Category
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from forms.models import General
import datetime
import json
from django.http import JsonResponse


# Create your views here.


class CandidatelListView(TemplateView):
    template_name = "training/candidate_table.html"

    def get_context_data(self):
        context = super(CandidatelListView, self).get_context_data()
        can_list = TesCandidate.objects.all().order_by("-id")
        context['can_list'] = can_list
        return context
    
class NewCandidatelView(TemplateView):
    template_name = "training/new_candidate.html"


    def get_context_data(self):
        context = super(NewCandidatelView, self).get_context_data()
        lastCan = TesCandidate.objects.last()
        tempID = int(lastCan.tes_candidate_id.split('-')[1])+1
        tempID = 'TESN-'+str(tempID)
        print(tempID)
        context['tesId'] = tempID
        return context
    
    

    def post(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'POST':
            print(request.POST['tes_id'])
            firstName =request.POST['first_name']
            lastName =request.POST['last_name']
            result = TesCandidate.objects.filter(first_name=firstName,last_name= lastName ).count()
            if result> 0 :
                print('exist')
                response = JsonResponse({"error": "there was an error"})
                response.status_code = 403 # To announce that the user isn't allowed to publish
                
                return render(request, 'training/errors.html') 
            user = User()
            user.username = request.POST['email']
            user.password =make_password(request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            # user.tes_candidate_id = request.POST['tesCanID']
            user.tescandidate.first_name = request.POST['first_name']
            user.tescandidate.middleName = request.POST['middleName']
            user.tescandidate.last_name = request.POST['last_name']
            user.tescandidate.birth_date = datetime.datetime.strptime(request.POST['birthDate'], '%m/%d/%Y')
            user.tescandidate.tes_candidate_id = request.POST['tes_id']
            user.tescandidate.customer_id = request.POST['customer_id']
            user.tescandidate.address = request.POST['address']
            # user.passport_id = request.POST['passport_id']
            user.tescandidate.sponsor_company = request.POST['sponsor_company']
            user.tescandidate.email = request.POST['email']
            user.tescandidate.contact_number = request.POST['phone']
            # user.note = request.POST['note']
            if request.FILES.get('photo', False):
                user.tescandidate.photo = request.FILES['photo']
            if request.FILES.get('doc_1', False):
                user.tescandidate.document_1 = request.FILES['doc_1']
            if request.FILES.get('doc_2', False):
                user.tescandidate.document_2 = request.FILES['doc_2']
            if request.FILES.get('doc_3', False):
                user.tescandidate.document_3 = request.FILES['doc_3']
            if request.FILES.get('doc_4', False):
                user.tescandidate.document_4 = request.FILES['doc_4']
            if request.FILES.get('doc_5', False):
                user.tescandidate.document_5 = request.FILES['doc_5']
            if request.FILES.get('doc_6', False):
                user.tescandidate.document_6 = request.FILES['doc_6']
            if request.FILES.get('doc_7', False):
                user.tescandidate.document_7 = request.FILES['doc_7']
            if request.FILES.get('doc_8', False):
                user.tescandidate.document_8 = request.FILES['doc_8']
            if request.FILES.get('doc_9', False):
                user.tescandidate.document_9 = request.FILES['doc_9']
            if request.FILES.get('doc_10', False):
                user.tescandidate.document_10= request.FILES['doc_10']
            user.save() 
        return redirect('training:canlist_')


class UpdateCandidatelView(TemplateView):
    template_name = "training/update_candidate.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateCandidatelView, self).get_context_data()
        can = TesCandidate.objects.filter(id = self.kwargs['id']).first()
        context['can'] = can

        return context

    def post(self, request, *args, **kwargs):
        # form = MedicineForm(self.request.POST)
        if request.method == 'POST':
            print('OK')
            
            user = TesCandidate.objects.filter(id = self.kwargs['id']).first()
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.middleName = request.POST['middleName']
            user.tes_candidate_id = request.POST['tes_id']
            user.customer_id = request.POST['customer_id']
            user.address = request.POST['address']
            user.birth_date = datetime.datetime.strptime(request.POST['birthDate'], '%m/%d/%Y')
            # user.passport_id = request.POST['passport_id']
            user.sponsor_company = request.POST['sponsor_company']
            user.email = request.POST['email']
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
        can = TesCandidate.objects.filter(id = self.kwargs['id']).first()
        context['can'] = can

        return context

    def get(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'GET':
            print('Del Here')
            can = TesCandidate.objects.filter(id = self.kwargs['id']).first()
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
        categoryList = Category.objects.all()
        context['event_list'] = event_list
        context['product_list'] = product_list
        context['lecturers_list'] = lecturers_list
        context['country_list'] = country_list
        context['location_list'] = location_list
        context['categoryList'] = categoryList

        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # country = Country.objects.get(id = request.POST['country'])
            product = Product.objects.get(id = request.POST['product'])
            lecturers = Lecturer.objects.get(id = request.POST['lecturer'])
            location = Location.objects.get(id = request.POST['location'])
            category = Category.objects.get(id = request.POST['category'])
            generalObj = General()

            obj = Event()
            obj.name = request.POST['name']
            obj.product = product
            obj.lecturers = lecturers
            obj.location = location
            obj.formCategory = category
            obj.country = location.country
            
            
            obj.start_date = datetime.datetime.strptime(request.POST['start_date'], '%m/%d/%Y')
            obj.practicalDate = datetime.datetime.strptime(request.POST['practicalDate'], '%m/%d/%Y')
            obj.save()  
            generalObj.event= obj
            generalObj.formCategory= category
            generalObj.save()

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
        categoryList = Category.objects.all()
        context['event'] = event
        context['product_list'] = product_list
        context['lecturers_list'] = lecturers_list
        context['country_list'] = country_list
        context['location_list'] = location_list
        context['categoryList'] = categoryList

        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
           
            print(request.POST['category'])
            product = Product.objects.get(id = request.POST['product'])
            lecturers = Lecturer.objects.get(id = request.POST['lecturer'])
            location = Location.objects.get(id = request.POST['location'])
            category = Category.objects.get(name__exact = request.POST['category'])
            obj = Event.objects.filter(id = self.kwargs['id']).first()
            obj.name = request.POST['name']
            obj.product = product
            obj.lecturers = lecturers
            obj.location = location
            obj.formCategory = category
            obj.country = location.country
            # obj.start_date = request.POST['start_date']
            obj.practicalDate = datetime.datetime.strptime(request.POST['practicalDate'], '%m/%d/%Y')
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


class NewAttendeesView(TemplateView):
    template_name = "training/attendees.html"

    def get_context_data(self, *args, **kwargs):
        selectedList = []
        context = super(NewAttendeesView, self).get_context_data()
        event = Event.objects.filter(id=self.kwargs['id']).first()
        can_list = TesCandidate.objects.order_by('first_name')
        selCan='{'
        selCounter = 0
        
        

        counter = 0
        can='{'
        for item in can_list:
            can =can + '"'+ str(counter)+'":"'+ str(item.tes_candidate_id)+' - '+ str(item.first_name)+' '+ str(item.last_name)+'--'+ '",'
            counter = counter + 1 
        can = can + '"10000000000":" "}'
        
       
        # print(can[0])

        
        for item in event.candidate.all():
            selCan =selCan + '"'+ str(selCounter)+'":"'+ str(item.tes_candidate_id)+' - '+ str(item.first_name)+' '+ str(item.last_name)+'",'
            selCounter = selCounter + 1 
        selCan = selCan + '"10000000000":" "}'
        
        myDict = json.loads(can)
        values = []
        
        for item in event.candidate.all():
            print(item.tes_candidate_id)
            for index,value in myDict.items():
                if str(item.tes_candidate_id) in value:
                    # print('Here: '+index)
                    values.append(int(index))
            
        
        context['selectedList'] = values
        context['can_list'] = can
        context['eventName'] = event.name

        return context
    
    def post(self, request, *args, **kwargs):
      
        if request.method == 'POST':
            # print( request.POST.get('page_contents[]', None))
            
            event = Event.objects.filter(id=self.kwargs['id'] ).first()
            event.candidate.clear()
            canList =request.POST['temp']
            
            if canList :
                for item in canList.split('--'):
                    can_id =item.split(' ')[0]
                    print('Now: '+can_id)
                    candidate = TesCandidate.objects.filter(tes_candidate_id__exact =can_id).first()
                    if candidate :
                        event.candidate.add(candidate)
                    # event.save()
                    
                
            
        return redirect('training:event_')


class NewEventLecturerView(TemplateView):
    template_name = "training/lecturer_events.html"

    def get_context_data(self, *args, **kwargs):
        selectedList = []
        context = super(NewEventLecturerView, self).get_context_data()
        print(self.kwargs['id'])
        lecturer = Lecturer.objects.filter(id=self.kwargs['id']).first()
        eventList = Event.objects.order_by('name').all()
        selLec='{'
        selCounter = 0
        print(lecturer)
        for item in lecturer.events.all():
            selLec =selLec + '"'+ str(selCounter)+'":"'+ str(item.id)+' - '+ str(item.name)+'",'
            selCounter = selCounter + 1 
        selLec = selLec + '"10000000000":" "}'
        
        
        counter = 0
        events='{'
        for item in eventList:
            events =events + '"'+ str(counter)+'":"'+ str(item.id)+' - '+ str(item.name)+'--",'
            counter = counter + 1 
        events = events + '"10000000000":" "}'
        # context['selectedList'] = selCan

        myDict = json.loads(events)
        values = []
        
        for item in lecturer.events.all():
            print(item.name)
            for index,value in myDict.items():
                if str(item.name) in value:
                    # print('Here: '+index)
                    values.append(int(index))
                    
        context['eventList'] = events
        context['lecturer'] = lecturer
        context['selectedList'] = values

        return context
    
    def post(self, request, *args, **kwargs):
        print('Here')
        if request.method == 'POST':
            # print( request.POST.get('page_contents[]', None))
            
            lecturer = Lecturer.objects.filter(id=self.kwargs['id']).first()
            lecturer.events.clear()
            eventList =request.POST['temp']
            print(eventList)
            
           
            if eventList :
                for item in eventList.split('--'):
                    event_id =item.split(' ')[0]
                    if event_id :
                        print('--> '+event_id)
                        event = Event.objects.filter(id = event_id).first()
                        print('here')
                        if event: 
                            print('Exist')
                            lecturer.events.add(event)
                        
                    
                
            
        return redirect('training:lecturer_')

class NewLecturerView(TemplateView):
    template_name = "training/new_lecturer.html"

    def get_context_data(self, *args, **kwargs):
        context = super(NewLecturerView, self).get_context_data()
        lecturer_list = Lecturer.objects.all()
        context['lecturer_list'] = lecturer_list

        return context

    def post(self, request, *args, **kwargs):
        # form = MedicineForm(self.request.POST)
        if request.method == 'POST':
            print('OK')
            
            lecturer = Lecturer()
            lecturer.first_name = request.POST['first_name']
            lecturer.last_name = request.POST['last_name']
            lecturer.email = request.POST['email']
            if request.POST.get('city', False):
                lecturer.city = request.POST['city']
                
            if request.POST.get('country', False):
                lecturer.country = request.POST['country']
                
            if request.POST.get('address', False):
                lecturer.address = request.POST['address']

            if request.POST.get('phone', False):
                lecturer.contact_number = request.POST['phone']
                print(request.POST['phone'])
                
            if request.POST.get('note', False):
                lecturer.note = request.POST['note']
            # lecturer.tes_candidate_id = request.POST['tes_id']
            # lecturer.customer_id = request.POST['customer_id']
            # lecturer.address = request.POST['address']
            # # user.passport_id = request.POST['passport_id']
            # lecturer.sponsor_company = request.POST['sponsor_company']
            # lecturer.email = request.POST['email']
            # lecturer.contact_number = request.POST['phone']
            # user.note = request.POST['note']
            if request.FILES.get('photo', False):
                lecturer.photo = request.FILES['photo']
            if request.FILES.get('doc_1', False):
                lecturer.document_1 = request.FILES['doc_1']
            if request.FILES.get('doc_2', False):
                lecturer.document_2 = request.FILES['doc_2']
            if request.FILES.get('doc_3', False):
                lecturer.document_3 = request.FILES['doc_3']
            if request.FILES.get('doc_4', False):
                lecturer.document_4 = request.FILES['doc_4']
            if request.FILES.get('doc_5', False):
                lecturer.document_5 = request.FILES['doc_5']
            if request.FILES.get('doc_6', False):
                lecturer.document_6 = request.FILES['doc_6']
            if request.FILES.get('doc_7', False):
                lecturer.document_7 = request.FILES['doc_7']
            if request.FILES.get('doc_8', False):
                lecturer.document_8 = request.FILES['doc_8']
            if request.FILES.get('doc_9', False):
                lecturer.document_9 = request.FILES['doc_9']
            lecturer.save() 
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
            
            if request.POST.get('city', False):
                obj.city = request.POST['city']
                
            if request.POST.get('country', False):
                obj.country = request.POST['country']
                
            if request.POST.get('address', False):
                obj.address = request.POST['address']

            if request.POST.get('phone', False):
                obj.contact_number = request.POST['phone']
                print(request.POST['phone'])
                
            if request.POST.get('note', False):
                obj.note = request.POST['note']
                
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
            obj.address = request.POST['address']
            obj.postalCode = request.POST['postalCode']
            obj.log = request.POST['longitude']
            obj.lat = request.POST['latitude']
            obj.city = request.POST['city']
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
            obj.address = request.POST['address']
            obj.postalCode = request.POST['postalCode']
            obj.city = request.POST['city']
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
        adminStatus=False
        context = super(TrainingPanelView, self).get_context_data()
        event_list = Event.objects.all()
        canCount = TesCandidate.objects.count()
        lecCount = Lecturer.objects.count()
        product = Product.objects.all()

        for g in self.request.user.groups.all():
            if  g.name == 'super_admin' or g.name=='training_admin':
                adminStatus=True
                print(g.name)
        context['event_list'] = event_list
        context['eventCount'] = event_list.count()
        context['canCount'] = canCount
        context['lecCount'] = lecCount
        context['product'] = product
        context['proCount'] = product.count()
        context['adminStatus'] = adminStatus

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
