from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from training.models import Event,Country,Location,Product,Lecturer,TesCandidate,Category,FormsList as Guideline,CourseRequest
from django.contrib.auth.models import User,Group
from django.contrib.auth.hashers import make_password
from forms.models import General,FormList,TwiEnrolmentForm,PSL30InitialForm,PSL30LogExp,PSL57A,NDTCovid19,NDT15AExperienceVerification,BGAsExperienceForm
import datetime
from datetime import  timedelta,timezone
import json
from django.http import JsonResponse
from  authorization.sidebarmixin import SidebarMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from contacts.models import Contact
from mailer.views import sendMail
# Create your views here.


class CandidatelListView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "training/candidate_table.html"

    def get_context_data(self):
        context = super(CandidatelListView, self).get_context_data()
        # can_list = TesCandidate.objects.filter(user__groups__name__in=['candidates',] )
        print("Here AMir!")
        can_list = TesCandidate.objects.all()
        context['can_list'] = can_list

        return context



class AllRequestView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "training/request_list.html"

    def get_context_data(self):
        context = super(AllRequestView, self).get_context_data()
        requests = CourseRequest.objects.all()
        context['requests'] =requests
        return context



class RequestView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "training/request_course.html"

    def get_context_data(self):
        context = super(RequestView, self).get_context_data()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()
        context['userID'] =candidate.id
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # country = Country.objects.get(id = request.POST['country'])
            obj = CourseRequest()
            obj.candidate = self.request.user
            obj.request = request.POST['request']
            obj.save()

            return redirect('accounting:canprofile_',id=request.POST['userID'])


class UserFormMonitor(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "training/user_form_monitor.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UserFormMonitor, self).get_context_data()
        userID = self.kwargs['id']
        candidate = TesCandidate.objects.filter(id = userID).first()
        events = Event.objects.filter(candidate = candidate)
        formList = FormList.objects.filter(candidate = candidate)

        mapFromList = []
        canFromList = []
        mainList = []
        formDict = dict()

        finalList = []

        for item in formList:
            canFromList.append(item.name)

        # for item in events:
        #     print(item.name)
        #     temooList = []
        #     for item2 in item.formCategory.form.all():
        #         if item2.name in canFromList:
        #             form = FormList.objects.filter(name=item2.name).first()
        #             print(form.id)
        #
        #             temooList.append({'name': item2.name,'status':True,'confirmation':form.status})
        #         else:
        #             temooList.append({'name': item2.name, 'status': False})
        #     mainList.append({'event': item.name, 'forms': temooList})
                # tempDict = {'form':item2.name}
                # finalList.



        # print(mainList)


        context['candidate'] = candidate
        context['events'] = events
        context['mainList'] = mainList

        return context


class NewCandidatelView(SidebarMixin,LoginRequiredMixin,TemplateView):
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
            group =Group.objects.filter(id=2).first()

            user.username = request.POST['email']
            user.password =make_password(request.POST['password'])
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.save()
            user.groups.add(group)
            # user.tes_candidate_id = request.POST['tesCanID']
            user.tescandidate.first_name = request.POST['first_name']
            user.tescandidate.middleName = request.POST['middleName']
            user.tescandidate.last_name = request.POST['last_name']
            user.tescandidate.birth_date = datetime.datetime.strptime(request.POST['birthDate'], '%m/%d/%Y')
            user.tescandidate.tes_candidate_id = request.POST['tes_id']
            user.tescandidate.customer_id = request.POST['customer_id']
            user.tescandidate.address = request.POST['address']
            # user.passport_id = request.POST['passport_id']
            user.tescandidate.emergencyContact = request.POST['emergencyContact']
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


class UpdateCandidatelView(SidebarMixin,LoginRequiredMixin,TemplateView):
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


class DeleteCandidatelView(SidebarMixin,LoginRequiredMixin,TemplateView):
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
    
    
class ProductView(SidebarMixin,LoginRequiredMixin,TemplateView):
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


    
class UpdateProductView(SidebarMixin,LoginRequiredMixin,TemplateView):
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



class DeleteProductView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "training/update.html"



    def get(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'GET':
            print('Del Here')
            product = Product.objects.filter(id = self.kwargs['id']).first()
            print(product.name)
            product.delete()
            return redirect('training:product_')


    
class EventView(SidebarMixin,LoginRequiredMixin,TemplateView):
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
            categories = Category.objects.filter(pk__in = request.POST.getlist('category'))


            generalObj = General()

            obj = Event()
            obj.name = request.POST['name']
            obj.product = product
            obj.lecturers = lecturers
            obj.location = location
            # obj.formCategory = category
            obj.country = location.country
            

            obj.start_date = datetime.datetime.strptime(request.POST['start_date'], '%m/%d/%Y')
            if not request.POST.get('practicalDate', None) == '':
                obj.practicalDate = datetime.datetime.strptime(request.POST['practicalDate'], '%m/%d/%Y')
            obj.save()
            for item in categories:
                obj.formCategory.add(item)
            # generalObj.event= obj
            # generalObj.formCategory= category
            # generalObj.save()



        return redirect('training:event_')

class UpdateEventView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "training/update_event.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateEventView, self).get_context_data()
        event = Event.objects.filter(id = self.kwargs['id']).first()
        product_list = Product.objects.all()
        lecturers_list = Lecturer.objects.all()
        country_list = Country.objects.all()
        location_list = Location.objects.all()
        categoryList = Category.objects.all()

        categorylist = Category.objects.order_by('name')
        print("Hello Amir")
        selForms = '{'

        counter = 0
        formList = '{'
        for item in categorylist:
            formList = formList + '"' + str(counter) + '":"' + str(item.name) + '--' + '",'
            counter = counter + 1

            tempdict = {}

        formList = formList + '"10000000000":" "}'

        values = []
        for item in event.formCategory.all():
            for i, j in enumerate(formList.split('--')):
                tesID = j.split(':')[1].split(' -')[0][1:]
                print(tesID)
                if tesID == item.name:
                    print(str(i) + " : " + tesID)
                    values.append(i)
                    selForms = selForms + '"' + str(i) + '":"' + str(item.name) + '",'

        selForms = selForms + '"10000000000":" "}'

        myDict = json.loads(selForms)

        context['selectedList'] = values
        context['formList'] = formList

        context['event'] = event
        context['product_list'] = product_list
        context['lecturers_list'] = lecturers_list
        context['country_list'] = country_list
        context['location_list'] = location_list
        context['categoryList'] = categoryList

        return context
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
           
            print("Hello Radin")
            product = Product.objects.get(id = request.POST['product'])
            lecturers = Lecturer.objects.get(id = request.POST['lecturer'])
            location = Location.objects.get(id = request.POST['location'])
            # category = Category.objects.get(name__exact = request.POST['category'])
            obj = Event.objects.filter(id = self.kwargs['id']).first()
            obj.name = request.POST['name']
            obj.product = product
            obj.lecturers = lecturers
            obj.location = location
            obj.country = location.country
            # obj.start_date = request.POST['start_date']
            # obj.practicalDate = datetime.datetime.strptime(request.POST['practicalDate'], '%m/%d/%Y')
            # if not request.POST.get('practicalDate', None) == '':
            #     obj.practicalDate = datetime.datetime.strptime(request.POST['practicalDate'], '%m/%d/%Y')
            obj.save()

            categoryList = request.POST['catList']
            obj.formCategory.clear()
            if categoryList:
                for item in categoryList.split('--'):
                    cat_name = item.split('--')[0]
                    print('Now: ' + cat_name)
                    category = Category.objects.filter(name__exact=cat_name).first()

                    if category:
                        obj.formCategory.add(category)


        return redirect('training:event_')


class DeleteEventView(SidebarMixin,LoginRequiredMixin,TemplateView):
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

            
class LecturerView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "training/lecturer_list.html"

    def get_context_data(self):
        context = super(LecturerView, self).get_context_data()
        lecturer_list = Lecturer.objects.all()
        context['lecturer_list'] = lecturer_list

        return context


class NewAttendeesView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "training/attendees.html"

    def get_context_data(self,id, *args, **kwargs):
        selectedList = []
        context = super(NewAttendeesView, self).get_context_data()
        event = Event.objects.filter(id=self.kwargs['id']).first()
        can_list = TesCandidate.objects.order_by('first_name')
        print("Here Amir")
        print(event)
        selCan='{'
     
        


        counter = 0
        can='{'
        for item in can_list:
            can =can + '"'+ str(counter)+'":"'+ str(item.tes_candidate_id)+' - '+ str(item.first_name)+' '+ str(item.last_name)+'--'+ '",'
            counter = counter + 1

            tempdict={}

        can = can + '"10000000000":" "}'




        for item in event.candidate.all():
            for i, j in enumerate(can.split('--')):
                tesID =j.split(':')[1].split(' -')[0][1:]
                if tesID == item.tes_candidate_id:
                    print(str(i) + " : " + tesID)
                    selCan =selCan + '"'+ str(i)+'":"'+ str(item.tes_candidate_id)+' - '+ str(item.first_name)+' '+ str(item.last_name)+'",'

        selCan = selCan + '"10000000000":" "}'
        
        myDict = json.loads(selCan)

        values = []
        
        for item in event.candidate.all():
            print(item.tes_candidate_id)
            for index,value in myDict.items():
                if str(item.tes_candidate_id) in value:
                    # print('Here: '+index)
                    values.append(int(index))
            
        
        context['selectedList'] = values
        context['can_list'] = can
        context['event'] = event

        return context
    
    def post(self, request, *args, **kwargs):
      
        if request.method == 'POST':
            # print( request.POST.get('page_contents[]', None))
            event = Event.objects.filter(id=self.kwargs['id'] ).first()
            event.candidate.clear()
            canList =request.POST['temp']
            catID = request.POST['catID']
            category = Category.objects.filter(id=catID).first()
            guidelineID = 1
            guideline = Guideline.objects.filter(id=guidelineID).first()



            if canList :
                for item in canList.split('--'):
                    can_id =item.split(' ')[0]

                    candidate = TesCandidate.objects.filter(tes_candidate_id__exact =can_id).first()
                    if candidate :
                        event.candidate.add(candidate)
                    # event.save()


                        for item in category.form.all():
                            print("======")
                            print(item.name)
                            print("======")
                            twiEnrolForm = TwiEnrolmentForm.objects.filter(candidate=candidate).first()
                            # bgasinitialForm = BGASinitialForm.objects.filter(candidate=candidate).first()
                            psl30LogExp = PSL30LogExp.objects.filter(candidate=candidate).first()
                            psl57A = PSL57A.objects.filter(candidate=candidate).first()
                            covid = NDTCovid19.objects.filter(candidate=candidate).first()
                            ndt15A = NDT15AExperienceVerification.objects.filter(candidate=candidate).first()
                            bgas = BGAsExperienceForm.objects.filter(candidate=candidate).first()

                            if item.name == 'TWI Enrolment Form':
                                if not twiEnrolForm:
                                    obj = TwiEnrolmentForm()
                                    print("Inside")
                                    print(candidate.first_name)
                                    obj.candidate = candidate
                                    obj.firstName = candidate.first_name
                                    obj.middleName = candidate.middleName
                                    obj.lastName = candidate.last_name
                                    obj.event=event
                                    obj.save()
                                    print(obj.id)


                                    formListObj = FormList()
                                    formListObj.name = obj.__class__.__name__
                                    formListObj.event = event
                                    formListObj.candidate = candidate
                                    formListObj.category = category
                                    formListObj.guideline = guideline
                                    formListObj.FormID = obj.id
                                    formListObj.save()


                                    contactObj =Contact()
                                    contactObj.type="Admin"
                                    contactObj.messageType="Form"
                                    contactObj.department="Registration"
                                    contactObj.message="Please fill following form: " + formListObj.name
                                    contactObj.formName = formListObj.name
                                    contactObj.objID=obj.id
                                    contactObj.candidate = candidate
                                    contactObj.save()

                                    fullname = candidate.first_name + " " + candidate.last_name
                                    msg = "Please login to your panel and fill the form :" + formListObj.name
                                    sendMail(candidate.email, fullname, msg)

                            if item.name == 'PSL-57A Initial exam application':
                                if not psl57A:
                                    obj = PSL57A()
                                    print("Inside 57A")
                                    print(candidate.first_name)
                                    obj.candidate = candidate
                                    obj.event=event
                                    obj.category=category
                                    obj.guideline=guideline
                                    obj.save()
                                    print(obj.id)


                                    formListObj = FormList()
                                    formListObj.name = obj.__class__.__name__
                                    formListObj.event = event
                                    formListObj.candidate = candidate
                                    formListObj.category = category
                                    formListObj.guideline = guideline
                                    formListObj.FormID = obj.id
                                    formListObj.save()


                                    contactObj =Contact()
                                    contactObj.type="Admin"
                                    contactObj.messageType="Form"
                                    contactObj.department="Registration"
                                    contactObj.message="Please fill following form: " + formListObj.name
                                    contactObj.formName=formListObj.name
                                    contactObj.objID=obj.id
                                    contactObj.candidate = candidate
                                    contactObj.save()

                                    fullname = candidate.first_name + " " + candidate.last_name
                                    msg = "Please login to your panel and fill the form :" + formListObj.name
                                    sendMail(candidate.email, fullname, msg)

                            if item.name == 'PSL-30_Log of experience':
                                if not psl30LogExp:
                                    obj = BGAsExperienceForm()
                                    print("Inside PSL-30-Log Experience")
                                    print(candidate.first_name)
                                    obj.candidate = candidate
                                    obj.event=event
                                    obj.save()
                                    print(obj.id)


                                    formListObj = FormList()
                                    formListObj.name = obj.__class__.__name__
                                    formListObj.event = event
                                    formListObj.candidate = candidate
                                    formListObj.category = category
                                    formListObj.guideline = guideline
                                    formListObj.FormID = obj.id
                                    formListObj.save()


                                    contactObj =Contact()
                                    contactObj.type="Admin"
                                    contactObj.messageType="Form"
                                    contactObj.department="Registration"
                                    contactObj.message="Please fill following form: " + formListObj.name
                                    contactObj.formName=formListObj.name
                                    contactObj.objID=obj.id
                                    contactObj.candidate = candidate
                                    contactObj.save()

                                    fullname = candidate.first_name + " " + candidate.last_name
                                    msg = "Please login to your panel and fill the form :" + formListObj.name
                                    sendMail(candidate.email, fullname, msg)

                            if item.name == 'COVID-19':
                                if not covid:
                                    obj = NDTCovid19()
                                    print("COVID-19")
                                    print("Inside Covid")
                                    print(candidate.first_name)
                                    obj.candidate = candidate
                                    obj.category = category
                                    obj.guideline = guideline
                                    obj.event = event
                                    obj.save()
                                    print(obj.id)

                                    formListObj = FormList()
                                    formListObj.name = obj.__class__.__name__
                                    formListObj.event = event
                                    formListObj.candidate = candidate
                                    formListObj.category = category
                                    formListObj.guideline = guideline
                                    formListObj.FormID = obj.id
                                    formListObj.save()

                                    print(candidate.email)
                                    contactObj = Contact()
                                    contactObj.type = "Admin"
                                    contactObj.messageType = "Form"
                                    contactObj.department = "Registration"
                                    contactObj.message = "Please fill following form: " + formListObj.name
                                    contactObj.formName = formListObj.name
                                    contactObj.objID = obj.id
                                    contactObj.candidate = candidate
                                    contactObj.save()

                                    fullname = candidate.first_name + " " + candidate.last_name
                                    msg = "Please login to your panel and fill the form :" + formListObj.name
                                    sendMail(candidate.email, fullname, msg)


                            if item.name == 'NDT 15A':
                                if not ndt15A:
                                    obj = NDT15AExperienceVerification()
                                    print("NDT 15A")
                                    print("Inside ")
                                    print(candidate.first_name)
                                    obj.candidate = candidate
                                    obj.category = category
                                    obj.guideline = guideline
                                    obj.event = event
                                    obj.save()
                                    print(obj.id)

                                    formListObj = FormList()
                                    formListObj.name = obj.__class__.__name__
                                    formListObj.event = event
                                    formListObj.candidate = candidate
                                    formListObj.category = category
                                    formListObj.guideline = guideline
                                    formListObj.FormID = obj.id
                                    formListObj.save()

                                    print(candidate.email)
                                    contactObj = Contact()
                                    contactObj.type = "Admin"
                                    contactObj.messageType = "Form"
                                    contactObj.department = "Registration"
                                    contactObj.message = "Please fill following form: " + formListObj.name
                                    contactObj.formName = formListObj.name
                                    contactObj.objID = obj.id
                                    contactObj.candidate = candidate
                                    contactObj.save()

                                    fullname = candidate.first_name + " " + candidate.last_name
                                    msg = "Please login to your panel and fill the form :" + formListObj.name
                                    sendMail(candidate.email, fullname, msg)

                            if item.name == 'BGAS_Experience_Form':
                                if not bgas:
                                    obj = BGAsExperienceForm()
                                    print("bgas")
                                    print("Inside bgas")
                                    print(candidate.first_name)
                                    obj.candidate = candidate
                                    obj.category = category
                                    obj.guideline = guideline
                                    obj.event = event
                                    obj.save()
                                    print(obj.id)

                                    formListObj = FormList()
                                    formListObj.name = obj.__class__.__name__
                                    formListObj.event = event
                                    formListObj.candidate = candidate
                                    formListObj.category = category
                                    formListObj.guideline = guideline
                                    formListObj.FormID = obj.id
                                    formListObj.save()

                                    print(candidate.email)
                                    contactObj = Contact()
                                    contactObj.type = "Admin"
                                    contactObj.messageType = "Form"
                                    contactObj.department = "Registration"
                                    contactObj.message = "Please fill following form: " + formListObj.name
                                    contactObj.formName = formListObj.name
                                    contactObj.objID = obj.id
                                    contactObj.candidate = candidate
                                    contactObj.save()

                                    fullname = candidate.first_name + " " + candidate.last_name
                                    msg = "Please login to your panel and fill the form :" + formListObj.name
                                    sendMail(candidate.email, fullname, msg)

        return redirect('training:event_')


class NewEventLecturerView(SidebarMixin,LoginRequiredMixin,TemplateView):
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

class NewLecturerView(SidebarMixin,LoginRequiredMixin,TemplateView):
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


class DeleteLecturerView(SidebarMixin,LoginRequiredMixin,TemplateView):
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



class UpdateLecturerView(SidebarMixin,LoginRequiredMixin,TemplateView):
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




class CountryView(SidebarMixin,LoginRequiredMixin,TemplateView):
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

class DeleteCountryView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "training/update.html"



    def get(self, request, *args, **kwargs):
    
        # form = MedicineForm(self.request.POST)
        if request.method == 'GET':
            print('Del Here')
            country = Country.objects.filter(id = self.kwargs['id']).first()
            print(country.name)
            country.delete()
            return redirect('training:country_')

class UpdateCountryView(SidebarMixin,LoginRequiredMixin,TemplateView):
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


class LocationView(SidebarMixin,LoginRequiredMixin,TemplateView):
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



class UpdateLocationView(SidebarMixin,LoginRequiredMixin,TemplateView):
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


class DeleteLocationView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "training/update.html"


    def get(self, request, *args, **kwargs):
        # form = MedicineForm(self.request.POST)
        if request.method == 'GET':
            print('Del Here')
            loc = Location.objects.filter(id = self.kwargs['id']).first()
            
            loc.delete()
            return redirect('training:location_')

class TrainingPanelView(SidebarMixin,LoginRequiredMixin,TemplateView):
    template_name = "training/layouts-vertical.html"

    def get_context_data(self):
        context = super(TrainingPanelView, self).get_context_data()
        event_list = Event.objects.all()[:3]
        eventCount = Event.objects.all().count()
        canCount = TesCandidate.objects.count()
        lecCount = Lecturer.objects.count()
        product = Product.objects.all()[:3]
        productCount = Product.objects.all().count()
        today = datetime.datetime.now()

        canPerMonth = TesCandidate.objects.filter(created_at__month=today.month).count()
        eventPerMonth = Event.objects.filter(created_at__month=today.month).count()
        lecturerPerMonth = Lecturer.objects.filter(created_at__month=today.month).count()
        productPerMonth = Product.objects.filter(created_at__month=today.month).count()
        candidate = TesCandidate.objects.filter(user=self.request.user).first()

        context['event_list'] = event_list
        context['candidate'] = candidate
        context['eventCount'] = event_list.count()
        context['canCount'] = canCount
        context['canPerMonth'] = (canPerMonth/canCount) * 100
        if event_list.count() >0 :
            context['eventPerMonth'] = (eventPerMonth/eventCount) * 100
        context['productPerMonth'] = (productPerMonth/productCount) * 100
        context['lecCount'] = lecCount
        context['lecturerPerMonth'] =  (lecturerPerMonth/lecCount) * 100
        context['product'] = product
        context['proCount'] = product.count()
        return context


    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            if 'searchBtn' in request.POST:
                keyword= request.POST['keyword']
                q_object = ~Q()
                eventQ_object = ~Q()
                kewordList = keyword.split(" ")
                for item in kewordList:
                    q_object |= Q(first_name__icontains=item) | (Q(middleName__icontains=item)) | (Q(last_name__icontains=item))
                    print(item)
                queryset = TesCandidate.objects.filter(q_object)


                for item in kewordList:
                    eventQ_object |= Q(name__icontains=item) | Q(country__name__icontains=item)
                eventQueryset = Event.objects.filter(eventQ_object)

                adminStatus = False
                for g in self.request.user.groups.all():
                    if g.name == 'super_admin' or g.name == 'training_admin':
                        adminStatus = True

                return render(request, 'training/search_result.html', {'searchResult': queryset, 'eventQueryset':eventQueryset,'adminStatus':adminStatus})


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


class FormCategoryView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "training/category_list.html"

    def get_context_data(self):
        context = super(FormCategoryView, self).get_context_data()
        category_list = Category.objects.all()
        form_list = Guideline.objects.all()
        context['category_list'] = category_list
        context['form_list'] = form_list

        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            guideID = request.POST['guideline']
            guidelineForm = Guideline.objects.filter(id = guideID).first()
            obj = Category()
            obj.name = request.POST['name']
            obj.save()
            obj.form.add(guidelineForm)
        return redirect('training:category_')


class FormCategoryDeleteView(SidebarMixin, LoginRequiredMixin,DeleteView):
    model = Category
    success_url = reverse_lazy('training:category_')


class UpdateFormCategoryView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "training/update_category.html"

    def get_context_data(self ,catID,*args, **kwargs):
        context = super(UpdateFormCategoryView, self).get_context_data()
        category = Category.objects.filter(id=self.kwargs['catID']).first()
        form_list = Guideline.objects.all()
        context['category'] = category
        context['form_list'] = form_list

        return context

    def post(self, request,catID, *args, **kwargs):
        if request.method == 'POST':
            categoryObj = Category.objects.filter(id = catID).first()
            categoryObj.name = request.POST['name']
            categoryObj.save()
        return redirect('training:category_')



class FormGuidelineView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "training/guideline_list.html"

    def get_context_data(self):
        context = super(FormGuidelineView, self).get_context_data()
        form_list = Guideline.objects.all()
        context['form_list'] = form_list

        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            obj = Guideline()
            obj.name = request.POST['name']
            obj.save()
        return redirect('training:guideline_')


class FormGuidelineDeleteView(SidebarMixin, LoginRequiredMixin,DeleteView):
    model = Guideline
    success_url = reverse_lazy('training:guideline_')

class UpdateFormGuidelineView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "training/update_guideline.html"

    def get_context_data(self ,id,*args, **kwargs):
        context = super(UpdateFormGuidelineView, self).get_context_data()
        guideline = Guideline.objects.filter(id=self.kwargs['id']).first()
        context['guideline'] = guideline
        return context

    def post(self, request,id, *args, **kwargs):
        if request.method == 'POST':
            guidelineObj = Guideline.objects.filter(id = id).first()
            guidelineObj.name = request.POST['guideName']
            guidelineObj.save()
        return redirect('training:guideline_')


class AddFormToCategoryView(SidebarMixin, LoginRequiredMixin, TemplateView):
    template_name = "training/add_form_category.html"

    def get_context_data(self, *args, **kwargs):
        selectedList = []
        context = super(AddFormToCategoryView, self).get_context_data()
        category = Category.objects.filter(id=self.kwargs['id']).first()
        form_list = Guideline.objects.order_by('name')
        print("Here Amir")
        selForms = '{'

        counter = 0
        formList = '{'
        for item in form_list:
            formList = formList + '"' + str(counter) + '":"' + str(item.name)  + '--' + '",'
            counter = counter + 1

            tempdict = {}

        formList = formList + '"10000000000":" "}'
        values = []
        for item in category.form.all():
            for i, j in enumerate(formList.split('--')):
                tesID = j.split(':')[1].split(' -')[0][1:]
                print(tesID)
                if tesID == item.name:
                    print(str(i) + " : " + tesID)
                    values.append(i)
                    selForms = selForms + '"' + str(i) + '":"' + str(item.name) + '",'

        selForms = selForms + '"10000000000":" "}'

        myDict = json.loads(selForms)


        context['selectedList'] = values
        context['formList'] = formList
        context['category'] = category.name

        return context

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            # print( request.POST.get('page_contents[]', None))

            category = Category.objects.filter(id=self.kwargs['id']).first()
            category.form.clear()
            canList = request.POST['temp']

            if canList:
                for item in canList.split('--'):
                    can_id = item.split('--')[0]
                    print('Now: ' + can_id)
                    candidate = Guideline.objects.filter(name__exact=can_id).first()
                    if candidate:
                        category.form.add(candidate)
                    # event.save()

        return redirect('training:category_')


